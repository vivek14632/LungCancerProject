# Author: Vivek Singh
# Check this for more information : https://keras.io/getting-started/sequential-model-guide/
# Purpose: Sample Keras code to build first Sequential model

# import packages
from keras.models import Dense
from keras.models import Sequential

# create a sequential model
model=Sequential()

# add first layer with RELU activation function
model.add(Dense(32, input_dim=784))
model.add(Activation('relu'))



