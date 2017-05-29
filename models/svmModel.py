import sklearn as sk
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

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

def run_svm():
    # Declare a list of all possible kernels in svm.SVC
    kernels = ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']
    for kernel in kernels:
        print('Running {} kernel'.format(kernel))
        clf = svm.SVC(kernel=kernel)
        clf.fit(train_x,train_y)
        pred = clf.predict(test_x)
        cm = confusion_matrix(test_y, pred)
        print('Confusion matrix for {} is \n {}'.format(kernel,cm))
    
def main():
    run_svm()
    
if __name__ == '__main__':
    main()
