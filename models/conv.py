import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

from scikits.statsmodels.tools import categorical

from data import *
from load_data import *
from train_test_split import *
X,Y = load_data()
train_x,test_x = get_train_test_data(X)
train_y,test_y = get_train_test_data(Y)

keep_rate = 0.8
keep_prob = tf.placeholder(tf.float32)

n_classes = 2
batch_size = 100

test_counter=0
def next_batch(batch_size):
	global test_counter
	batch_counter=test_counter
	#global test_counter
	test_counter=(batch_counter+1)
	return train_x[batch_counter:(batch_counter+batch_size),:], categorical(train_y[batch_counter:(batch_counter+batch_size)][:,0],drop=True)


x = tf.placeholder('float',[None,X.shape[1]])
y = tf.placeholder('float')

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def maxpool2d(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

def cnn(x):
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

    fc = tf.reshape(conv2,[-1, 32*32*256])

    fc = tf.nn.relu(tf.matmul(fc, weights['w_fc'])+biases['b_fc'])
    fc = tf.nn.dropout(fc, keep_rate)
    fc = tf.nn.dropout(fc, keep_rate)
    
    output = tf.matmul(fc, weights['out'])+biases['out']

    return output

def train_nueral_network(x):
	
	prediction = convolution_nueral_network	(x)


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


train_nueral_network(x)