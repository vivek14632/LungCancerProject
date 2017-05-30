from sklearn import svm
from sklearn import neighbors
from sklearn.metrics import confusion_matrix

def run_knn():
    knn.fit(train_x,train_y)
    pred = knn.predict(test_x)
    cm = confusion_matrix(test_y, pred)
    print('Confusion matrix is \n {}'.format(cm))
