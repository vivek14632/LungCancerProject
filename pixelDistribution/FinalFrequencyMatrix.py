import dicom
import os
import pandas as pd
import numpy as np

user=os.getlogin()
def print_final_matrix():
	destination_dir=''
	data_dir=''
	if(user=='vivek4'):
		destination_dir = '/work/v/vivek4/stage1_clean_bak_X_matrix/'
		data_dir = '/work/v/vivek4/stage1_clean_bak/'
	else:
		print('Log: Please specify your path')

	patients = os.listdir(data_dir)

	#count total number of slices
	total_slices = 0
	for patient in patients[:]:
		print(patient)
		print('total slice='+str(total_slices))
		
		mat = np.load(data_dir + patient)
		total_slices += len(mat)

	#define final freq matrix
	final_matrix = np.zeros(total_slices*4097, dtype = int).reshape(total_slices,4097)
	patient_label = np.ndarray(total_slices*1, dtype = object).reshape(total_slices,1)	
	#print final_matrix

	#Lets keep track of row in the final matrix
	finalMatrixRowCounter=0

	for patient in patients[:]:
		mat_new = np.load(data_dir + patient)
		for each in range(len(mat_new)):
			
			#go to each slice and get frequency matrix
			x = mat_new[each]
			unique, counts = np.unique(x, return_counts=True)
			freq_mat= np.asarray((unique, counts)).T    
			#update final matrix numpy array
			for j in range(len(freq_mat)):
				final_matrix[finalMatrixRowCounter][freq_mat[j][0]] = freq_mat[j][1]
			#Adding new column with patient label
			patient_label[finalMatrixRowCounter] = str(patient)
			#updating the counter
			
			finalMatrixRowCounter=finalMatrixRowCounter+1
	#print final_matrix
	#save matrix
	np.save(destination_dir + 'final_matrix',final_matrix)
	np.save(destination_dir + 'patient_label',patient_label)

print_final_matrix()
