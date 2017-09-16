import tensorflow as tf
import numpy as np
import keras as ks
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

model = Sequential()

#Conv Layer 1
model.add(Conv2D(,(), input_shape = ()))
model.add(Activation('relu'))
#Pooling Layer 1
model.add(MaxPooling2D(pool_size = ()))

#Conv Layer 2
model.add(Conv2D(,(), input_shape = ()))
model.add(Activation('relu'))
#Pooling Layer 2
model.add(MaxPooling2D(pool_size = ()))

#Conv Layer 3
model.add(Conv2D(,(), input_shape = ()))
model.add(Activation('relu'))

#Conv Layer 4
model.add(Conv2D(,(), input_shape = ()))
model.add(Activation('relu'))
#Pooling Layer 4
model.add(MaxPooling2D(pool_size = ()))


#This converts our 3D feature maps to 1D feature vectors
#Fully Connected layer 1
model.add(Dense(64))
model.add(Flatten())  
model.add(Activation('relu'))
#Dropout Layer
model.add(Dropout(0.5))
#Fully Connected layer 2
model.add(Dense(1))
model.add(Activation('sigmoid'))

