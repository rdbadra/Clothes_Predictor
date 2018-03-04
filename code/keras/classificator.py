from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input, Flatten, Dense
from keras.models import Model
from keras.models import Sequential
import numpy as np
import pandas as pd
import os

def convert_image(path):
    img = image.load_img(os.getcwd()+"/../../crops/"+path, target_size=(150, 200))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def process_line(line):
    split = line.split()
    image = convert_image(split[0])
    Y = []
    Y.append(int(split[1]))
    y_np = np.zeros(14)
#Falta hacer one hot encode
    return image, y_np



def generate_arrays_from_file(path):
    while 1:
        with open(path) as f:
            line = f.readline()
            line = f.readline()
            line = f.readline()
            while line:
                # create Numpy arrays of input data
                # and labels, from each line in the file
                x, y = process_line(line)
                yield (x, y)
                line = f.readline()

#Get back the convolutional part of a VGG network trained on ImageNet
model_vgg16_conv = VGG16(weights='imagenet', include_top=False)
#model_vgg16_conv.summary()

#Create your own input format (here 3x200x200)
input = Input(shape=(150,200, 3),name = 'image_input')

#Use the generated model 
output_vgg16_conv = model_vgg16_conv(input)

#Add the fully-connected layers 
x = Flatten(name='flatten')(output_vgg16_conv)
x = Dense(4096, activation='relu', name='fc1')(x)
x = Dense(4096, activation='relu', name='fc2')(x)
x = Dense(14, activation='softmax', name='predictions')(x)

#Create your own model 
my_model = Model(inputs=input, outputs=x)

#In the summary, weights and layers from VGG part will be hidden, but they will be fit during the training
#my_model.summary()
my_model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
my_model.fit_generator(generate_arrays_from_file(os.getcwd()+"/../../subsets/subset1.txt"),
                    steps_per_epoch=1000, epochs=10)


#Then training with your data !