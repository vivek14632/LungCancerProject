import sklearn
from sklearn import svm
from sklearn import neighbors
from sklearn.metrics import confusion_matrix

from load_data import *
from train_test_split import *

def run_knn(train_x,train_y,test_x,test_y):
	knn=neighbors.KNeighborsClassifier(n_neighbors=2)
	knn.fit(train_x,train_y)
	pred = knn.predict(test_x)
	cm = confusion_matrix(test_y, pred)
	print('Confusion matrix is \n {}'.format(cm))
	
def main():
	X,Y = load_data()
	# Create train and test data
	train_x,test_x = get_train_test_data(X)
	print('Train and test data created for X matrix created with dimensions {} and {} respectively'.format(train_x.shape,test_x.shape))

	train_y,test_y = get_train_test_data(Y)
	print('Train and test data created for Y matrix created with dimensions {} and {} respectively'.format(train_y.shape,test_y.shape))
	
	# Run knn model
	run_knn(train_x,train_y,test_x,test_y)
	
if __name__ == '__main__':
    main()
