# LungCancerProject


# Run process in back ground

nohup python <file.py> & 

It will create a nohup.out file with logs

# check if process is running

ps -ef|grep <Linux_username>

# X matrix

/home/ravi/final_matrix.npy

# Y matrix

/home/cis1024/sample_images_Y.npy

# Proposed changes and Instructions to Run Y-Matrix Generator Python file
python y_matrix_generator.py arg1 arg2 arg2
where arg1 -> Fully qualified path of directory containing all image files.
      arg2 -> Directory path where the final numpy matrix needs to be saved
      arg3 -> Fully qualified path of file containing all image labels.

Example Command line execution
python y_matrix_generator.py D:\Learning\Cancer_Project\Data\sample_images_clean D:\Docs D:\Learning\Cancer_Project\Data\stage1_labels.csv

Note : So far, code changes have been made only to accept the first two arguments. 
      Changes to accomodate arg3 are to be made after checking if get_label(x) function of readLabel.py is referenced anywhere
      else in the project.
      
Example code for current changes
python y_matrix_generator.py D:\Learning\Cancer_Project\Data\sample_images_clean D:\Docs
