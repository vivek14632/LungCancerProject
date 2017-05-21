# author: vivek

# this code is used to store the numpy matrix

#create a numpy matrix

import numpy as np

def saveNumpy(mObject, mFileName):
	image=np.zeros((1000,10))
	np.save(mFileName,mObject)


#test code
if __name__ == '__main__':
	image=np.zeros((1000,10))
	saveNumpy(image,'hello')




