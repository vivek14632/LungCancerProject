import os
user= os.getlogin()
if(user=='cis1024'):
	X_MAT_PATH='/home/ravi/final_matrix.npy'
	Y_MAT_PATH='/home/cis1024/sample_images_Y.npy'
elif (user=='root'or user=='vivek4'):
	#X_MAT_PATH='/work/v/vivek4/final_matrix.npy'
	#Y_MAT_PATH='/work/v/vivek4/sample_images_Y.npy'
	Y_MAT_PATH='/work/v/vivek4/stage1_clean_bak_Y_matrix/sample_images.npy'
	#X_MAT_PATH='/work/v/vivek4/stage1_clean_bak_X_matrix/final_matrix.npy'
	PATIENT_MAT_PATH = '/work/v/vivek4/stage1_clean_bak_Y_matrix/patient_label_matrix.npy'
	# Lets change the path after feature reduction
	X_MAT_PATH='/work/v/vivek4/stage1_clean_bak_X_matrix_after_featureReduction/stage1_clear_bak_X_matrix_afterFR.npy'
	# Following is the processed image folder on circe
	STAGE1_CLEAN_BAK='/work/v/vivek4/stage1_clean_bak'
elif (user=='vivek'):
	#X_MAT_PATH='/work/v/vivek4/final_matrix.npy'
	#Y_MAT_PATH='/work/v/vivek4/sample_images_Y.npy'
	Y_MAT_PATH='/home/vivek/stage1_clean_bak_Y_matrix/sample_images.npy'
	#X_MAT_PATH='/work/v/vivek4/stage1_clean_bak_X_matrix/final_matrix.npy'
	#Lets change the path after feature reduction
	X_MAT_PATH='/home/vivek/stage1_clean_bak_X_matrix_after_featureReduction/stage1_clear_bak_X_matrix_afterFR.npy'
	# Following is the processed image folder on circe
	STAGE1_CLEAN_BAK='/work/v/vivek4/stage1_clean_bak'
	PATIENT_MAT_PATH = '/home/vivek/stage1_clean_bak_Y_matrix/patient_label_matrix.npy'
elif (user=='deepak'):
	X_MAT_PATH='/work/v/vivek4/final_matrix.npy'
	Y_MAT_PATH='/work/v/vivek4/sample_images_Y.npy'
elif (user=='ravi'):
	X_MAT_PATH='/work/v/vivek4/final_matrix.npy'
	Y_MAT_PATH='/work/v/vivek4/sample_images_Y.npy'
elif (user=='rhomi'):
	X_MAT_PATH='D:\Learning\Cancer_Project\Data\Final X And Y Matrices\final_matrix.npy'
	Y_MAT_PATH='D:\Learning\Cancer_Project\Data\Final X And Y Matrices\sample_images_Y.npy' 
else:
	print("Error: Please specifiy data path")
