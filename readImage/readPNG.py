# https://stackoverflow.com/questions/31386096/importing-png-files-into-numpy

# pip install scipy

# install the numpy from following website: http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

import scipy
import numpy
from scipy import misc
import glob
image=misc.imread('C:/Users/vivek4/Desktop/top.png')
image


import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
