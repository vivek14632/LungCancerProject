import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

from scikits.statsmodels.tools import categorical

from data import *
from load_data import *
from train_test_split import *
X,Y, y_patient = load_data()
train_x,test_x = get_train_test_data(X)
train_y,test_y = get_train_test_data(Y)



# vivek: what is the format of data in /temp/data? dicom or normal images?
#mnist = input_data.read_data_sets("/temp/data/", one_hot = True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

# vivek: for our code, i think there will be 2 classes.
#n_classes = 10
n_classes = 2
# vivek: what is batch_size?
# vivek: batch_size is used to give data to training in batch, see the forloop in the bottom
batch_size = 100

test_counter=0
def next_batch(batch_size):
	global test_counter
	batch_counter=test_counter
	#global test_counter
	test_counter=(batch_counter+1)
	return train_x[batch_counter:(batch_counter+batch_size),:], categorical(train_y[batch_counter:(batch_counter+batch_size)][:,0],drop=True)

#hieght*width
# vivek: I guess 784 is coming from 28*28, right?. In out case, the it will be 4095

x = tf.placeholder('float',[None,X.shape[1]])

#placeholder for y variables which is class
y = tf.placeholder('float')


def nueral_network_model(data):

	hidden_1_layer = {'weights':tf.Variable(tf.random_normal([X.shape[1],n_nodes_hl1])),
					  'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

	hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1,n_nodes_hl2])),
					  'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

	hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2,n_nodes_hl3])),
					  'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

	output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3,n_classes])),
					  'biases':tf.Variable(tf.random_normal([n_classes]))}
	# (input_data*weights) + biases

	l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']),hidden_1_layer['biases'])
	l1 = tf.nn.relu(l1)

	l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']),hidden_2_layer['biases'])
	l2 = tf.nn.relu(l2)

	l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']),hidden_3_layer['biases'])
	l3 = tf.nn.relu(l3)

	output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

	return output

def train_nueral_network(x):
	
	prediction = nueral_network_model(x)


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
