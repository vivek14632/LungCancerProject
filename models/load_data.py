import sklearn as sk
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

from data import*
from train_test_split import *

def load_data():
	X = np.load(X_MAT_PATH)
	Y = np.load(Y_MAT_PATH)
	Y_PATIENT = np.load(PATIENT_MAT_PATH)
	print("X matrix with shape {} has been loaded".format(X.shape))
	print("Y matrix with shape {} has been loaded".format(Y.shape))
	print("Y_PATIENT matrix with shape {} has been loaded".format(Y_PATIENT.shape))
	# Converting dtype to int32
	X = X.astype(int)
	Y = Y.astype(int)
	return X,Y,Y_PATIENT
