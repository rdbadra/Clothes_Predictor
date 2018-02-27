from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input, Flatten, Dense
from keras.models import Model
from keras.models import Sequential
import numpy as np

#Get back the convolutional part of a VGG network trained on ImageNet
model_vgg16_conv = VGG16(weights='imagenet', include_top=False)
#model_vgg16_conv.summary()

#Use the generated model 
output_vgg16_conv = model_vgg16_conv(input)

#Add the fully-connected layers 
model = Sequential()
model.add(Flatten(input_shape=(224,224,3)))
model.add(Dense(4096, activation='relu'))
model.add(Dense(4096, activation='relu', name='fc2'))
model.add(Dense(14, activation='softmax', name='predictions'))

#Create your own model 
my_model = Model(inputs=input, outputs=model)

#In the summary, weights and layers from VGG part will be hidden, but they will be fit during the training
my_model.summary()


#Then training with your data !