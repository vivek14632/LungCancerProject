from sklearn import svm
from sklearn import neighbors
from sklearn.metrics import confusion_matrix

from load_data import *
from train_test_split import *
from load_data import *
from svmModel import *

import timeit
from datetime import datetime

def run_knn():
	X,Y = load_data()

	# Create train and test data
	train_x,test_x = get_train_test_data(X)
	print('Train and test data for X matrix created with dimensions {} and {} respectively'.format(train_x.shape,test_x.shape))

	train_y,test_y = get_train_test_data(Y)
	print('Train and test data for Y matrix created with dimensions {} and {} respectively'.format(train_y.shape,test_y.shape))
	
	# The fit method of the estimator expects a 1d array and not a column-vector (which is what test_y is now). Change the shape of test_y to (n_samples, )
	train_y = reshape_label_matrix(train_y)
	
	# Get the start time
	start = timeit.default_timer()
	start_time = datetime.now()
	print('Execution started at {}'.format(start_time))
	
	knn=neighbors.KNeighborsClassifier(n_neighbors=3)
	knn.fit(train_x,train_y)
	pred = knn.predict(test_x)
	cm = confusion_matrix(test_y, pred)
	print('Confusion matrix : \n {}'.format(cm))
	
	# Get the stop time
	stop = timeit.default_timer()
	stop_time = datetime.now()
	print('Execution ended at {}'.format(stop_time))
	print('Total Execution time : {}'.format(stop - start))
	print('-----------------------------------------------')
	
def main():
	# Run knn model
	run_knn()
	
if __name__ == '__main__':
    main()
