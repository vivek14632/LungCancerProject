import numpy as np

import sklearn as sk
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

import timeit
from datetime import datetime

from data import * 
from train_test_split import *
from load_data import *


def reshape_label_matrix(matrix_object):
    c, r = matrix_object.shape
    matrix_object = matrix_object.reshape(c,)
    return matrix_object

def svm_cv(folds):

	data = load_data()
	
	X = data[0]
	Y= data[1]

	# Create train and test data
	train_x,test_x = get_train_test_data(X)
	print('Train and test data for X matrix created with dimensions {} and {} respectively'.format(train_x.shape,test_x.shape))

	train_y,test_y = get_train_test_data(Y)
	print('Train and test data for Y matrix created with dimensions {} and {} respectively'.format(train_y.shape,test_y.shape))
	
	# Reshape the Y label matrix to have a shape like array(r,). This is required for running cross-validation.
	train_y = reshape_label_matrix(train_y)

	# Declare a list of all possible kernels in svm.SVC
	kernels = ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']
	for kernel in kernels:
		print('Running {} kernel'.format(kernel))
		clf = svm.SVC(kernel=kernel)
		# Get the start time
		start = timeit.default_timer()
		start_time = datetime.now()
		print('Execution started at {}'.format(start_time))

		# Perform cross-validation
		# Run cross-validation
		for k in folds:
			print('Performing cross validation with {} folds'.format(k))
			scores = cross_val_score(clf, train_x, train_y, cv=k)
			print('The final accuracy scores are {}'.format(scores))
			print('Mean accuracy score for {} folds is {}'.format(k,scores.mean()))

		# Get the stop time
		stop = timeit.default_timer()
		stop_time = datetime.now()
		print('Execution ended at {}'.format(stop_time))
		print('Total Execution time : {}'.format(stop - start))
		print('-----------------------------------------------')

def run_svm():
	X,Y = load_data()

	# Create train and test data
	train_x,test_x = get_train_test_data(X)
	print('Train and test data for X matrix created with dimensions {} and {} respectively'.format(train_x.shape,test_x.shape))

	train_y,test_y = get_train_test_data(Y)
	print('Train and test data for Y matrix created with dimensions {} and {} respectively'.format(train_y.shape,test_y.shape))

	# The fit method of the estimator expects a 1d array and not a column-vector. Changing the shape of train_y(label matrix) to (n_samples, ).
	train_y = reshape_label_matrix(train_y)
	
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
		print('-----------------------------------------------')
        
    
def main():	
	run_svm()
	
	# Create a list of number of folds to be run
	folds = [5,10,15,20]
	svm_cv(folds)
if __name__ == '__main__':
    main()
