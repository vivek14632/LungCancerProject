import numpy as np

import sklearn as sk
from sklearn import svm
from sklearn.metrics import confusion_matrix

import timeit
from datetime import datetime

from data import*
from train_test_split import *

X = np.load(X_MAT_PATH)
Y = np.load(Y_MAT_PATH)

print("X matrix with shape {} has been loaded".format(X.shape))
print("Y matrix with shape {} has been loaded".format(Y.shape))

# Converting dtype to int32
X = X.astype(int)
Y = Y.astype(int)

# Creating training and testing sets
train_x,test_x = get_train_test_data(X)
print('Train and test data created for X matrix created with dimensions {} and {} respectively'.format(train_x.shape,test_x.shape))

train_y,test_y = get_train_test_data(Y)
print('Train and test data created for Y matrix created with dimensions {} and {} respectively'.format(train_y.shape,test_y.shape))

def reshape_label_matrix(matrix_object):
    c, r = matrix_object.shape
    matrix_object = matrix_object.reshape(c,)
    return matrix_object

def svm_cv(train_x,train_y,folds):
    kernels = ['rbf', 'rbf']
    for kernel in kernels:
        print('Running {} kernel'.format(kernel))
        clf = svm.SVC(kernel=kernel)
        # Get the start time
        start = timeit.default_timer()
        start_time = datetime.now()
        print('Execution started at {}'.format(start_time))
        
        # Perform cross-validation
        print('Performing cross validation with {} folds'.format(folds))
        scores = cross_val_score(clf, test_x, test_y, cv=folds)
        print('The final accuracy scores are {}'.format(scores))
        print('Mean accuracy score for {} folds is {}'.format(folds,scores.mean()))
        
        # Get the stop time
        stop = timeit.default_timer()
        stop_time = datetime.now()
        print('Execution ended at {}'.format(stop_time))
        print('Total Execution time : {}'.format(stop - start))
        print('-----------------------------------------------')

def run_svm():
    # Declare a list of all possible kernels in svm.SVC
    kernels = ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']
    for kernel in kernels:
        print('Running {} kernel'.format(kernel))
        clf = svm.SVC(kernel=kernel)
        # Get the start time
        start = timeit.default_timer()
        start_time = datetime.now()
        print('Execution started at {}'.format(start_time))
        
        # Fit the model
        clf.fit(train_x,train_y)
        # Run predictions on the test data
        pred = clf.predict(test_x)
        # Create confusion matrix
        cm = confusion_matrix(test_y, pred)
        print('Confusion matrix for {} is \n {}'.format(kernel,cm))
        
        # Get the stop time
        stop = timeit.default_timer()
        stop_time = datetime.now()
        print('Execution ended at {}'.format(stop_time))
        print('Total Execution time : {}'.format(stop - start))
        
    
def main():
    run_svm()
    
    
    # Run cross-validation
    train_y = reshape_label_matrix(train_y)
    # Create a list of number of folds to be run
    folds = [5,10,15,20]
    for k in folds:
        svm_cv(train_x,train_y,k)
if __name__ == '__main__':
    main()
