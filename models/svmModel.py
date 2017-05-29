# svm model
import sklearn
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

from data import*

X = np.load(X_MAT_PATH)
y = np.load(Y_MAT_PATH)

x_len = X.shape[0]
print('Length of X is {}'.format(x_len))
y_len = y.shape[0]
print('Length of y is {}'.format(y_len))

y.dtype
# Converting dtype of y to int32 numpy array
y1 = y.astype(int)
y1.dtype
print('dtype of y1 is {}'.format(y1.dtype))
print('Number of 1s in y1 is {}'.format(sum(y1)))


# Run the model  
clf = svm.SVC()

# Run the model on 80% data
#@vivek: please remove the hard coded values
clf.fit(X[0:2727,], y1[0:2727])  

# Predict on 20%
#@vivek: please remove the hard coded values
pred = clf.predict(X[2728:X.shape[0]])

#@vivek: please remove the hard coded values
cm = confusion_matrix(y1[2728:y1.shape[0]], pred)
print('Confusion matrix \n'.format(cm))

# Do a reverse confustion matrix
#@vivek: please remove the hard coded values
cm = confusion_matrix(pred,y1[2728:y1.shape[0]])
print('Reverse Confusion matrix \n'.format(cm))
