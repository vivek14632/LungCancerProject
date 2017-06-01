import os
import numpy as np
import sys

from readLabel import *
from NumpyMatrix import *

# function to calculate number of images in each patient file.
def get_tot_images(file):
	print("Reading images from {0}".format(file))
	npy_file = np.load(file)
	dim = npy_file.shape
	print("{0} contains {1} images".format(file, dim))
	return(dim[0])
	
def matrix_generator(path):
	# Set it as the current working directory
	os.chdir(path)
	# Get all files in current working directory
	files = os.listdir(os.getcwd())
	num_imgs = []
	labels = []
	patient = []
	# create a list containing the number of images in each patient file.
	for file in files:
		num_imgs.append(get_tot_images(file))
	# create a list that contains the label(0 or 1) repeated n number of times (for each patient) 
	# where n is the number of images for each patient. And convert this list into a numpy array 
	# (there is a significant performance gain by doing it this way).
	for file, num in zip(files, num_imgs):    
		file_name, file_ext = file.split('.')
		print("Reading label for {0}".format(file_name))
		print('label='+str(get_label(file_name)))
		labels.append(get_label(file_name)*num)
		patient.append([file_name]*num)
	# Combine all the elements of the list into one giant string    
	single_label_string = ''.join(map(str, labels))
	# Convert the multi-columned matrix into a single-columned structure.
	final_patient_list = np.hstack(patient)
	# Cast the string into a list before assigning it to a numpy array. This results in a numpy 
	# matrix that has only one column and its rows as the label of each image of each patient.
	final_matrix = np.column_stack((list(single_label_string),final_patient_list))
	return final_matrix  

def save_numpy(matrix_object, file_name):
	np.save(matrix_object,file_name)
	
def main():
	#my_path=''
	#if(mUser=='vivek4'):
	#		my_path = '/work/v/vivek4/sample_images_clean/'
	
	# arg1 -> The path where all the image files exist
	filepath = sys.argv[1]
	# arg2 -> The path where the final npy matrix needs to be saved at
	finalpath = sys.argv[2]
	# arg3 -> Fully qualified path of file containing the image labels
	#labels_path = sys.argv[3]
	print("Reading files from {0}".format(filepath))
	# Get the numpy matrix by calling the matrix_generator function        
	final_matrix = matrix_generator(filepath)
	filename = 'patient_label_matrix.npy'
	file = os.path.join(finalpath, filename)
	saveNumpy(final_matrix, file)
	print("Numpy matrix has been saved as {}".format(file))
	print("Shape of the numpy matrix is {}".format(final_matrix.shape))
if __name__ == '__main__':
	main()
