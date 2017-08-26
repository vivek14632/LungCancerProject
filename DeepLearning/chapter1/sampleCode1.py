# import packages
from keras.models import Dense
from keras.models import Sequential

# create a sequential model
model=Sequential()

# add first layer with RELU activation function
model.add(Dense(32, input_dim=784))
model.add(Activation('relu'))

