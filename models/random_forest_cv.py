import numpy as np
import sklearn as sk
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier

from load_data import *
from train_test_split import *
from svmModel import *
from timer import *


def random_forest_cv(folds):

	X,Y = load_data()

	# Create train and test data
	train_x,test_x = get_train_test_data(X)
	print('Train and test data for X matrix created with dimensions {} and {} respectively'.format(train_x.shape,test_x.shape))

	train_y,test_y = get_train_test_data(Y)
	print('Train and test data for Y matrix created with dimensions {} and {} respectively'.format(train_y.shape,test_y.shape))

	# The fit method of the estimator expects a 1d array and not a column-vector (which is what test_y is now). Change the shape of test_y to (n_samples, )
	train_y = reshape_label_matrix(train_y)
	
	# Get the start time
	get_start_time()
	
	clf = RandomForestClassifier(n_estimators=500)
	
	# Run cross-validation
	for k in folds:
		print('Performing cross validation with {} folds'.format(k))
		scores = cross_val_score(clf, train_x, train_y, cv=k)
		print('The final accuracy scores are {}'.format(scores))
		print('Mean accuracy score for {} folds is {}'.format(k,scores.mean()))
	
	# Get the stop time
	get_stop_time()

def main():	

	# Create a list of number of folds to be run
	folds = [5,10,15,20]
	random_forest_cv(folds)
	
if __name__ == '__main__':
    main()
