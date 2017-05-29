user= os.getlogin()
if(user=='cis1024'):
  X_MAT_PATH='/home/ravi/final_matrix.npy'
  Y_MAT_PATH='/home/cis1024/sample_images_Y.npy'
elif (user=='vivek4'):
  X_MAT_PATH='/work/v/vivek4/final_matrix.npy'
  Y_MAT_PATH='/work/v/vivek4/sample_images_Y.npy'
  
else:
  print("Error: Please specifiy data path")
