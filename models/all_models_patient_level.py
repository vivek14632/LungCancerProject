import os
import numpy as np
import pandas as pd
import sklearn as sk

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
from sklearn import svm

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from load_data import *
from train_test_split import *
from timer import *
import sys



def svm_rbf(train_x, test_x, train_y, test_y):

    # Get the start time
    get_start_time()

    print_line()

    clf = svm.SVC(kernel='rbf')
    clf.fit(train_x,train_y[:,0])
    pred = clf.predict(test_x)
    cm = confusion_matrix(test_y[:,0], pred)
    print('Confusion matrix is \n {}'.format(cm))

    print_line()

    get_accuracy(test_y,pred)
    print_line()

    # Get the stop time
    get_stop_time()
    print_double_line()


def svm_linear(train_x, test_x, train_y, test_y):

    # Get the start time
    get_start_time()
    print_line()

    clf = svm.SVC(kernel='linear')
    clf.fit(train_x,train_y[:,0])
    pred = clf.predict(test_x)
    cm = confusion_matrix(test_y[:,0], pred)
    print('Confusion matrix is \n {}'.format(cm))
    print_line()

    get_accuracy(test_y,pred)
    print_line()

    # Get the stop time
    get_stop_time()
    print_double_line()

def random_forest(train_x, test_x, train_y, test_y):

    # Get the start time
    get_start_time()
    print_line()

    clf = RandomForestClassifier(n_estimators=500)
    clf = clf.fit(train_x, train_y[:,0])
    pred = clf.predict(test_x)
    cm = confusion_matrix(test_y[:,0], pred)
    print('Confusion matrix is \n {}'.format(cm))
    print_line()

    get_accuracy(test_y,pred)
    print_line()

    # Get the stop time
    get_stop_time()
    print_double_line()

def adabooster(train_x, test_x, train_y, test_y):

    # Get the start time
    get_start_time()
    print_line()

    clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=3),n_estimators=30)
    clf = clf.fit(train_x, train_y[:,0])
    pred = clf.predict(test_x)
    cm = confusion_matrix(test_y[:,0], pred)
    print('Confusion matrix is \n {}'.format(cm))
    print_line()

    get_accuracy(test_y,pred)
    print_line()

    # Get the stop time
    get_stop_time()
    print_double_line()


def naive_bayes(train_x, test_x, train_y, test_y):

    # Get the start time
    get_start_time()
    print_line()

    clf = GaussianNB()
    # Fit the model
    clf.fit(train_x,train_y[:,0])
    # Run predictions on the test data
    pred = clf.predict(test_x)
    # Create confusion matrix
    cm = confusion_matrix(test_y[:,0], pred)	
    print('Confusion matrix  {}'.format(cm))
    print_line()

    get_accuracy(test_y,pred)
    print_line()

    # Get the stop time
    get_stop_time()
    print_double_line()


def gradient_booster(train_x, test_x, train_y, test_y):
    # Get the start time
    get_start_time()
    print_line()

    gb = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0).fit(train_x,train_y[:,0])
    gb.score(train_x,train_y[:,0])
    pred = gb.predict(test_x)
    cm = confusion_matrix(test_y[:,0], pred)
    print('Confusion matrix : \n {}'.format(cm))
    print_line()

    get_accuracy(test_y,pred)
    print_line()

    # Get the stop time
    get_stop_time()
    print_double_line()

def knn(train_x, test_x, train_y, test_y):

    # Get the start time
    get_start_time()
    print_line()

    knn=neighbors.KNeighborsClassifier()
    knn.fit(train_x,train_y[:,0])
    pred = knn.predict(test_x)
    cm = confusion_matrix(test_y[:,0], pred)
    print('Confusion matrix is \n {}'.format(cm))
    print_line()

    get_accuracy(test_y,pred)
    print_line()

    # Get the stop time
    get_stop_time()
    print_double_line()

def get_accuracy(actual, predicted):
    pd.set_option('display.max_rows', 1000)
    df = pd.DataFrame(actual, columns=['actual label', 'patient'])
    df['predicted label'] = predicted
    unique_patients = df.patient.unique()
    for patient in unique_patients:
        df_temp = df[df['patient']==patient]
        indices = df_temp.loc[(df_temp['actual label'] != df_temp['predicted label'])].index
        misclassified = np.array(indices)
        print('Number of images for patient {} : {}'.format(patient,df_temp.shape[0]))
        print('Number of images misclassified : {}'.format(misclassified.shape[0]))
        print('Percentage of images misclassified : {:.1%}'.format(misclassified.shape[0]/df_temp.shape[0]))	

def print_line():
    print('----------------------------------------------------------------')

def print_double_line():
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')

def main():

    filepath = sys.argv[1]

    # Create a list of number of folds to be run
    folds = [5,10,15,20]

    print('Details about the data and train/test split')
    print_line()
    # Get all train and test sets of X and Y
    train_x, test_x, train_y, test_y = get_patient_train_test(filepath)
    print_line()
    # Run all models
    # Running svm_rbf
    #print('Running svm_rbf')
    #svm_rbf(train_x, test_x, train_y, test_y)

    print_line()
    # Running svm_linear
    #print('Running svm_linear')
    #svm_linear(train_x, test_x, train_y, test_y)

    print_line()
    # Running knn
    print('Running knn')
    knn(train_x, test_x, train_y, test_y)

    print_line()
    # Running gradient_booster
    print('Running gradient_booster')
    gradient_booster(train_x, test_x, train_y, test_y)

    print_line()
    # Running gaussian NB
    print('Running gaussian NB')
    naive_bayes(train_x, test_x, train_y, test_y)

    print_line()
    # Running adabooster
    print('Running adabooster')
    adabooster(train_x, test_x, train_y, test_y)

    print_line()
    # Running random_forest
    print('Running random_forest')
    random_forest(train_x, test_x, train_y, test_y)


if __name__ == '__main__':
    main()
