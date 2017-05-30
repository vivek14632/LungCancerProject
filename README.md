# LungCancerProject


# Run process in back ground

nohup python <file.py> & 

It will create a nohup.out file with logs

# check if process is running

ps -ef|grep <Linux_username>

# Image preprocessing

Provide the path to the raw files folder and the folder to store the images and run the following file.
https://github.com/vivek14632/LungCancerProject/blob/master/vivek/storeClearnedImpages.py

# X matrix

/home/ravi/final_matrix.npy

# Y matrix

/home/cis1024/sample_images_Y.npy

# X matrix generator Location

LungCancerProject/pixelDistribution/FinalFrequencyMatrix.py

# Y matrix generator Location

LungCancerProject/vivek/y_matrix_generator.py

# How to Run Y-Matrix Generator

python y_matrix_generator.py <arg1> <arg2>

where arg1 -> Fully qualified path of directory containing all image files.
      arg2 -> Directory path where the final numpy matrix needs to be saved.

Example Command line execution

python y_matrix_generator.py D:\Learning\Cancer_Project\Data\sample_images_clean D:\Docs

# How to genrate X- Matrix

TODO: @Ravi can you please update this section?

# How to run the models

TODO: Ravi and Deepak: Please update this section.


