from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import numpy as np
from data import *

x_dir =X_MAT_PATH
y_dir =Y_MAT_PATH

X = np.load(x_dir)
y = np.load(y_dir)

clf = MLPClassifier(solver='lbfgs', alpha=0.5,hidden_layer_sizes=(5, 2), random_state=1)

# comment: @ vivek: can we remove the hard coded values? Lets use 80 20 rule
clf.fit(X[:2000], y[:2000])                         


prediction = clf.predict(X[2000:3604])

cm = confusion_matrix(y[2000:3604],prediction)

#accuracy 64.4%
