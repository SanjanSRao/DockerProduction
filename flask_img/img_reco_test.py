# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:26:24 2019

@author: rao_s
"""

#Generating test images

from PIL import Image
from keras.datasets import mnist
import numpy as np
import keras
import os
os.environ['KERAS_BACKEND'] = 'theano'
(X_train, y_train), (X_test, y_test) = mnist.load_data()
for i in np.random.randint(0, 10000+1, 10):
    arr2im = Image.fromarray(X_train[i])
    arr2im.save('{}.png'.format(i), "PNG")