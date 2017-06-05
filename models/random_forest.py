from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier

from load_data import *
from train_test_split import *
from load_data import *
from svmModel import *
from timer import *

def run_random_forest():

	data = load_data()
	
	X = data[0]
	Y= data[1]

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
	clf = clf.fit(train_x, train_y)
	pred = clf.predict(test_x)
	cm = confusion_matrix(test_y, pred)
	print('Confusion matrix is \n {}'.format(cm))
	
	
	# Get the stop time
	get_stop_time()
	
def main():
	# Run random forest model
	run_random_forest()
	
if __name__ == '__main__':
    main()
