import tensorflow as tf
import numpy as np


# ## save to file
#
# W=tf.Variable([[1,2,3],[4,5,6]],dtype=tf.float32,name='weights')
# b=tf.Variable([[1,2,3]],dtype=tf.float32,name='biases')
#
# ## init
# init=tf.global_variables_initializer()
#
# ## define saver
# saver=tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init)
#     save_path=saver.save(sess,'my_net/save_net.ckpt')
#     print("save to path",save_path)


##restore variables
##redefine the same shape and same type for your variables

W=tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name="weights")
b=tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name="biases")


#saver
saver=tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess,"my_net/save_net.ckpt")
    print("weights:",sess.run(W))
    print("biases:", sess.run(b))
