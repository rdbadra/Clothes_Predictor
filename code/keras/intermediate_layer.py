import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential, load_model, Model
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from sklearn.metrics import confusion_matrix, accuracy_score
import itertools
import matplotlib.pyplot as plt
import pandas as pd

def getIntermediateModel():
  model = load_model('../../../Clothes_predictor_models/sequential_withRegularizerL2.h5')
  #model.summary()
  layer_name = 'fc1'
  intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.get_layer(layer_name).output)
  return intermediate_layer_model
  

def create_data():
  train_path = 'crops/train'
  valid_path = 'crops/valid'
  test_path = 'crops/test'

  classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Leggings', 'Romper', 'Shorts', 'Skirt', 'Sweater',
            'Tee', 'Top']
  train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(150,200), classes=classes, batch_size=32)
  valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(150,200), classes=classes, batch_size=32)
  test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(150,200), classes=classes, batch_size=1)
  return train_batches, valid_batches, test_batches

model = getIntermediateModel()
train_batches, valid_batches, test_batches = create_data()

test_super_labels= []
predictions = np.zeros(shape=(7000, 4096))
labels = np.zeros(shape=(7000, 14))
test_imgs, test_labels = next(test_batches)
i = 0
while (len(test_super_labels) < 7000):
  predictions[i] = model.predict(test_imgs, steps=1, verbose=0)
  labels[i] = test_labels
  test_super_labels = np.append(test_super_labels, np.argmax(test_labels))
  test_imgs, test_labels = next(test_batches)
  i += 1

np.savetxt('input.csv', predictions, delimiter=',')
np.savetxt('labels.csv', labels, delimiter=',')