# author: vivek

# this code is used to store and read the numpy matrix

#create a numpy matrix

import numpy as np

def saveNumpy(mObject, mFileName):
	image=np.zeros((1000,10))
	np.save(mFileName,mObject)

def readNumpy(mFileName):
	return np.load(mFileName)

#test code
if __name__ == '__main__':
	image=np.zeros((1000,10))
	saveNumpy(image,'hello')

	print(np.shape(readNumpy('hello.npy')))


