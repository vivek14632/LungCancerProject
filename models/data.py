import os
user= os.getlogin()
if(user=='cis1024'):
  X_MAT_PATH='/home/ravi/final_matrix.npy'
  Y_MAT_PATH='/home/cis1024/sample_images_Y.npy'
elif (user=='vivek4'):
  X_MAT_PATH='/work/v/vivek4/final_matrix.npy'
  Y_MAT_PATH='/work/v/vivek4/sample_images_Y.npy'
  
  # Following is the processed image folder on circe
  STAGE1_CLEAN_BAK='/work/v/vivek4/stage1_clean_bak'
elif (user=='deepak'):
  X_MAT_PATH='/work/v/vivek4/final_matrix.npy'
  Y_MAT_PATH='/work/v/vivek4/sample_images_Y.npy'
elif (user=='rhomi'):
  X_MAT_PATH='D:\Learning\Cancer_Project\Data\Final X And Y Matrices\final_matrix.npy'
  Y_MAT_PATH='D:\Learning\Cancer_Project\Data\Final X And Y Matrices\sample_images_Y.npy' 
else:
  print("Error: Please specifiy data path")
