#import tensorflow
import tensorflow as tf

#import numpy
import numpy as np

# vivek: why are you using mnist sample data? Should we just commen this code?
from tensorflow.examples.tutorials.mnist import input_data

# This will transform categorical variables to dummy variables
from scikits.statsmodels.tools import categorical

# To get dicom data
from data import *
from load_data import *

# split data into train test
from train_test_split import *

#load data
X,Y, Y_PATIENT = load_data()

#split data into train test
train_x,test_x = get_train_test_data(X)
train_y,test_y = get_train_test_data(Y)

# vivek: I guess the following is the learning rate?
keep_rate = 0.8

# place holder for probability? what is the use of this probability?
keep_prob = tf.placeholder(tf.float32)

# number of classes
n_classes = 2

# this the the data which we give each time for taining.
# vivek: can we vary this data and see if we get better accuracy?
batch_size = 100

#Batch processing - similar to nueral network

# vivek: what is the use of this test counter? I guess it is to
# keep track of global batch size
test_counter=0

def next_batch(batch_size):
	global test_counter
	batch_counter=test_counter
	#global test_counter
	test_counter=(batch_counter+1)
	
	# vivek: you should verify the outcome of the following code
	return train_x[batch_counter:(batch_counter+batch_size),:], categorical(train_y[batch_counter:(batch_counter+batch_size)][:,0],drop=True)


x = tf.placeholder('float',[None,X.shape[1]])
y = tf.placeholder('float')

def conv2d(x, w):
  return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')

def maxpool2d(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

def cnn(x):
	
# weights and biases are defined here. We have four convolution and four pool layers with relu activation.
# this can be further fine tuned by imcreasing the layers or changing the activation function.
    weights = {'w_conv1':tf.Variable(tf.random_normal([5,5,1,32])),
               'w_conv2':tf.Variable(tf.random_normal([5,5,32,64])),
               'w_conv3':tf.Variable(tf.random_normal([5,5,64,128])),
               'w_conv4':tf.Variable(tf.random_normal([5,5,128,256])),
               'w_fc':tf.Variable(tf.random_normal([32*32*256,1024])),
               'out':tf.Variable(tf.random_normal([1024, n_classes]))}

    biases = {'b_conv1':tf.Variable(tf.random_normal([32])),
              'b_conv2':tf.Variable(tf.random_normal([64])),
              'b_conv3':tf.Variable(tf.random_normal([128])),
              'b_conv4':tf.Variable(tf.random_normal([256])),
              'b_fc':tf.Variable(tf.random_normal([1024])),
              'out':tf.Variable(tf.random_normal([n_classes]))}

    x = tf.reshape(x, shape=[-1, 512, 512, 1])

    conv1 = tf.nn.relu(conv2d(x, weights['w_conv1']) + biases['b_conv1'])
    conv1 = maxpool2d(conv1)
    
    conv2 = tf.nn.relu(conv2d(conv1, weights['w_conv2']) + biases['b_conv2'])
    conv2 = maxpool2d(conv2)

    conv3 = tf.nn.relu(conv2d(conv2, weights['w_conv3']) + biases['b_conv3'])
    conv3 = maxpool2d(conv3)
    
    conv4 = tf.nn.relu(conv2d(conv3, weights['w_conv4']) + biases['b_conv4'])
    conv4 = maxpool2d(conv4)

#after pooling / feature reduction , final image size would be 32*32 with 256 features
    fc = tf.reshape(conv2,[-1, 32*32*256])
#relu activation is used here. Refer tensor flow documentation to change this function.
    fc = tf.nn.relu(tf.matmul(fc, weights['w_fc'])+biases['b_fc'])
    
    fc = tf.nn.dropout(fc, keep_rate)
    
    output = tf.matmul(fc, weights['out'])+biases['out']

    return output

#to train the network : similar to nueral network
def train_convolution_network(x):
	
	prediction = cnn(x)


	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=y))
	optimizer = tf.train.AdamOptimizer().minimize(cost)

	hm_epochs = 10

	with tf.Session() as sess:
		sess.run(tf.initialize_all_variables())

		for epoch in range(hm_epochs):
			epoch_loss = 0
			for i in range(int(len(train_x)/batch_size)):
				epoch_x,epoch_y = next_batch(batch_size)
				i, c = sess.run([optimizer, cost],feed_dict = {x: epoch_x,y: epoch_y})
				epoch_loss += c
			print('Epoch', epoch, 'completed out of', hm_epochs,'loss:', epoch_loss)


		correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
		accuracy = tf.reduce_mean(tf.cast(correct,'float'))
		print('Accuracy:', accuracy.eval({x:test_x, y:categorical(test_y[:,0],drop=True)}))


train_convolution_network(x)
