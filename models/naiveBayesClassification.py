# author: vivek
# Naive Bayes classification

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import timeit
from train_test_split import *

# load the data
X = np.load(X_MAT_PATH)
Y = np.load(Y_MAT_PATH)

# Converting dtype to int32
X = X.astype(int)
Y = Y.astype(int)

# Creating training and testing sets
train_x,test_x = get_train_test_data(X)
print('Train and test data created for X matrix created with dimensions {} and {} respectively'.format(train_x.shape,test_x.shape))

train_y,test_y = get_train_test_data(Y)
print('Train and test data created for Y matrix created with dimensions {} and {} respectively'.format(train_y.shape,test_y.shape))

def nb_cv(train_x,train_y,folds):
	clf = GaussianNB()
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


def run_nb():    
	
	clf = GaussianNB()
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
	run_nb()


	# Run cross-validation
	train_y = reshape_label_matrix(train_y)
	# Create a list of number of folds to be run
	folds = [5,10,15,20]
	for k in folds:
		nb_cv(train_x,train_y,k)
if __name__ == '__main__':
	main()

