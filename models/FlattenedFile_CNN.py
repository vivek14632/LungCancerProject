import numpy as np
import os

from NumpyMatrix import *

#data_dir = "C:/Users/maruv/Downloads/sample_images_clean/"

def main_matrix(data_dir):
    #define total slices
    total_slices = 0
    
    #define the patients directory
    patients = os.listdir(data_dir)
    
    #calculate completex slices for given set of patients
    for patient in patients[:]:
        mat = np.load(data_dir+'/'+patient)
        total_slices += len(mat)
		#print(total_slices)
    
    #define new matrix
    new_mat = np.ndarray(total_slices*1, dtype = object)
    return new_mat
    
   

def create_flat_mat(matrix,data_dir):
	new_counter = 0
	patients = os.listdir(data_dir)
	for patient in patients[:]:
		print('Processing ',patient)
		patient = np.load(data_dir+'/'+patient)

		#flatten matrix
		for i in range(patient.shape[0]):
			matrix[new_counter] = patient[i].ravel()
			new_counter += 1
			print('Counter ' + str(new_counter)+' '+str(len(matrix)))
	return matrix

def main():
	mat = main_matrix(data_dir)
	final_matrix = create_flat_mat(mat,data_dir)


	filename = 'flat_sample_py3.npy'
	file = os.path.join(r'C:/Users/maruv/Downloads/sample_images_clean/Final"', filename)

	saveNumpy(final_matrix, file)
	print("Numpy matrix has been saved as {}".format(file))
	print("Shape of the numpy matrix is {}".format(final_matrix.shape))
    
if __name__ == '__main__':
    main()
