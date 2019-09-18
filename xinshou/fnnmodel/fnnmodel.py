# coding:utf-8

import tensorflow as tf

def inputbatch(filename, batchsize=4):
    filenamequeues = tf.train.string_input_producer(filename, num_epochs=None)
    reader = tf.TextLineReader()
    key, value = reader.read(filenamequeues)
    record_defaults = [ [x] for x in [0.0]*10 ]  # 使用10个特征
    col1, col2, col3, label = tf.decode_csv(value, record_defaults=record_defaults)
    feature = tf.concat([["col"+str(x)] for x in range(10)])  # 这样做是不对的