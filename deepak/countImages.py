# To Get total count of images in the data.

import numpy as np
import os

# Change working directory
os.chdir(r'fully qualified path of the folder containing numpy files goes here')

# Get all files in current working directory
files = os.listdir(os.getcwd())

# Create a file dictionary and load the data files into it
file_dict = {}
for index,file in enumerate(files):
    file_dict[index] = np.load(file)

# Iterate over the file dictionary and count the number of images in each numpy.ndarray
for key, np_object in file_dict.items():
    dimensions = np_object.shape
    tot_images += dimensions[0]
