import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential, Model, load_model
from keras.layers import Activation, Dropout
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from sklearn.metrics import confusion_matrix, accuracy_score
import itertools
import matplotlib.pyplot as plt
import os

def create_model():
  vgg16 = keras.applications.vgg16.VGG16(weights='imagenet', input_shape=(224, 224, 3), include_top=False)

  model = Sequential()

  for layer in vgg16.layers:
      model.add(layer)

  #model.summary()

  #model.layers.pop()
  for layer in model.layers[:-4]:
    layer.trainable = False

  model.add(Flatten(name='flatten'))
  model.add(Dense(512, activation='relu', name='fc1'))
  model.add(BatchNormalization())
  model.add(Dropout(0.8))
  model.add(Dense(14, activation='softmax', name="output"))
  #model.summary()
  model.compile(keras.optimizers.Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
  return model

def create_data():
  folder = os.getcwd()+"/../../crops/"
  train_path = folder+'train'
  valid_path = folder+'valid'
  test_path = folder+'test'

  #classes = ['Jeans',  'Leggings', 'Shorts', 'Skirt']
  #classes = ['Blazer', 'Blouse', 'Cardigan', 'Jacket', 'Sweater','Tee', 'Top']
  classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Leggings', 'Romper', 'Shorts', 'Skirt', 'Sweater',
            'Tee', 'Top']
  #classes = ['full-body', 'lower-body', 'upper-body']
  #classes = ['Blazer', 'Jacket', 'Cardigan']
  #classes = ['Blouse', 'Sweater', 'Tee', 'Top']
  train_batches = ImageDataGenerator(rescale=1./255, rotation_range=25, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest").flow_from_directory(train_path, target_size=(224,224), classes=classes, batch_size=32)
  
  valid_batches = ImageDataGenerator(rescale=1./255).flow_from_directory(valid_path, target_size=(224,224), classes=classes, batch_size=32)
  
  test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(224,224), classes=classes, batch_size=1)
  return train_batches, valid_batches, test_batches
  
def plot_confusion(test_labels, predictions):
  classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Leggings', 'Romper', 'Shorts', 'Skirt', 'Sweater',
            'Tee', 'Top']
  #classes = ['Blazer', 'Blouse', 'Cardigan', 'Jacket', 'Sweater','Tee', 'Top']
  #classes = ['full-body', 'lower-body', 'upper-body']
  #classes = ['Blazer', 'Jacket', 'Cardigan']
  #classes = ['Blouse', 'Sweater', 'Tee', 'Top']
  cm_plot_labels = classes
  cm = confusion_matrix(test_labels, predictions)
  plot_confusion_matrix(cm, cm_plot_labels, title='Confusion Matrix')
  
  
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
def predict(model, test_batches):
  test_super_labels= []
  predictions = []
  test_imgs, test_labels = next(test_batches)
  while (len(test_super_labels) < 20874):
    predictions = np.append(predictions, np.argmax(model.predict(test_imgs, steps=1, verbose=0)))
    test_super_labels = np.append(test_super_labels, np.argmax(test_labels))
    test_imgs, test_labels = next(test_batches)

  plot_confusion(test_super_labels, predictions)
  print("accuracy score from prediction : ")
  print(accuracy_score(test_super_labels, predictions))
  return test_super_labels, predictions
def writeArffFile(name, end, classes):  
  with open(name+'.arff', 'w') as fp:
    fp.write("@RELATION Clothes_Predictor\n\n\n")
    for i in range(512):
      fp.write("@ATTRIBUTE "+"W"+str(i)+ " numeric\n")
    fp.write("@ATTRIBUTE type_of_cloth "+"{Blazer, Blouse, Cardigan, Dress, Jacket, Jeans, Jumpsuit, Leggings, Romper, Shorts, Skirt, Sweater,"+
              "Tee, Top}\n\n\n")
    fp.write("@DATA\n\n")
    for row in end:
      #print(row[4096])
      for i in range(len(row)):
        if i==(len(row)-1):
          #print(classes[int(row[i])])
          fp.write(classes[int(row[i])]+"\n")
        else:
          fp.write(str(row[i])+",")
          
def predict_top_3(model, test_batches):
  classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Leggings', 'Romper', 'Shorts', 'Skirt', 'Sweater',
            'Tee', 'Top']
  size = test_batches.samples
  test_super_labels= []
  predictions = []
  test_imgs, test_labels = next(test_batches)
  correct = 0
  total = 0
  while (len(test_super_labels) < size):
    #predictions = np.append(predictions, np.argmax(model.predict(test_imgs, steps=1, verbose=0)))
    answer = model.predict(test_imgs, steps=1, verbose=0)
    values = {}
    a, b = answer.shape
    for i in range(b):
      values[str(answer[0][i])] = i
    mostProb = classes[np.argmax(answer)]
    nextArr = np.delete(answer, np.argmax(answer))
    nextProb = classes[values[str(nextArr[np.argmax(nextArr)])]]
    nextArr = np.delete(nextArr, np.argmax(nextArr))
    nextProb2 = classes[values[str(nextArr[np.argmax(nextArr)])]]
    result = classes[np.argmax(test_labels)]
    if( result == mostProb or result == nextProb or result == nextProb2):
      correct += 1
    test_super_labels = np.append(test_super_labels, np.argmax(test_labels))
    test_imgs, test_labels = next(test_batches)
    total += 1
  print("Top-3 : ")
  print("correct answers = "+str(correct))
  print("Accuracy = "+str((correct/size)*100))
  
def predict_top_2(model, test_batches):
  classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Leggings', 'Romper', 'Shorts', 'Skirt', 'Sweater',
            'Tee', 'Top']
  size = test_batches.samples
  test_super_labels= []
  predictions = []
  test_imgs, test_labels = next(test_batches)
  correct = 0
  total = 0
  while (len(test_super_labels) < size):
    #predictions = np.append(predictions, np.argmax(model.predict(test_imgs, steps=1, verbose=0)))
    answer = model.predict(test_imgs, steps=1, verbose=0)
    values = {}
    a, b = answer.shape
    for i in range(b):
      values[str(answer[0][i])] = i
    mostProb = classes[np.argmax(answer)]
    nextArr = np.delete(answer, np.argmax(answer))
    nextProb = classes[values[str(nextArr[np.argmax(nextArr)])]]
    result = classes[np.argmax(test_labels)]
    if( result == mostProb or result == nextProb):
      correct += 1
    test_super_labels = np.append(test_super_labels, np.argmax(test_labels))
    test_imgs, test_labels = next(test_batches)
    total += 1
  print("Top-2 : ")
  print("correct answers = "+str(correct))
  print("Accuracy = "+str((correct/size)*100))
  
def predict_top_5(model, test_batches):
  classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Leggings', 'Romper', 'Shorts', 'Skirt', 'Sweater',
            'Tee', 'Top']
  size = test_batches.samples
  test_super_labels= []
  predictions = []
  test_imgs, test_labels = next(test_batches)
  correct = 0
  total = 0
  while (len(test_super_labels) < size):
    #predictions = np.append(predictions, np.argmax(model.predict(test_imgs, steps=1, verbose=0)))
    answer = model.predict(test_imgs, steps=1, verbose=0)
    values = {}
    a, b = answer.shape
    for i in range(b):
      values[str(answer[0][i])] = i
    mostProb = classes[np.argmax(answer)]
    nextArr = np.delete(answer, np.argmax(answer))
    nextProb = classes[values[str(nextArr[np.argmax(nextArr)])]]
    nextArr = np.delete(nextArr, np.argmax(nextArr))
    nextProb2 = classes[values[str(nextArr[np.argmax(nextArr)])]]
    nextArr = np.delete(nextArr, np.argmax(nextArr))
    nextProb3 = classes[values[str(nextArr[np.argmax(nextArr)])]]
    nextArr = np.delete(nextArr, np.argmax(nextArr))
    nextProb4 = classes[values[str(nextArr[np.argmax(nextArr)])]]
    
    result = classes[np.argmax(test_labels)]
    if( result == mostProb or result == nextProb or result == nextProb2 or result == nextProb3 or result == nextProb4):
      correct += 1
    #else:
      #print("expected : "+mostProb+", "+nextProb+", "+nextProb2+", "+nextProb3+", "+nextProb4)
      #print("real answer : "+result)
    test_super_labels = np.append(test_super_labels, np.argmax(test_labels))
    test_imgs, test_labels = next(test_batches)
    total += 1
  print("Top-5 : ")
  print("correct answers = "+str(correct))
  print("Accuracy = "+str((correct/size)*100))

def predict_ensemble(test_batches, full_model, lower_model, upper_model, flu_model):
  full_classes = ['Romper', 'Dress', 'Jumpsuit']
  lower_classes = ['Jeans', 'Leggings', 'Shorts', 'Skirt']
  upper_classes = ['Blazer', 'Blouse', 'Cardigan', 'Jacket', 'Sweater','Tee', 'Top']
  flu_classes = ['full-body', 'lower-body', 'upper-body']
  classes = ['Blazer', 'Blouse', 'Cardigan', 'Dress', 'Jacket', 'Jeans', 'Jumpsuit', 'Leggings', 'Romper', 'Shorts', 'Skirt', 'Sweater',
            'Tee', 'Top']
  size = test_batches.samples
  predictions = []
  labels = []
  test_imgs, test_labels = next(test_batches)
  correct = 0
  total = 0
  while (len(labels) < size):
    flu = flu_model.predict(test_imgs, steps=1, verbose=0)
    flu_a = np.argmax(flu)
    if (flu_a == 0):
      full = full_model.predict(test_imgs, steps=1, verbose=0)
      if (full_classes[np.argmax(full)] == classes[np.argmax(test_labels)]):
        correct += 1
    elif (flu_a == 1):
      lower = lower_model.predict(test_imgs, steps=1, verbose=0)
      if (lower_classes[np.argmax(lower)] == classes[np.argmax(test_labels)]):
        correct += 1
    else:
      upper = upper_model.predict(test_imgs, steps=1, verbose=0)
      if (upper_classes[np.argmax(upper)] == classes[np.argmax(test_labels)]):
        correct += 1
    labels = np.append(labels, np.argmax(test_labels))
    test_imgs, test_labels = next(test_batches)
    total += 1
  print("Ensemble prediction : ")
  print("Total samples = "+str(total))
  print("correct answers = "+str(correct))
  print("Accuracy = "+str((correct/size)*100))

filepath="upper-4-classes-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
early = keras.callbacks.EarlyStopping(monitor='val_loss',
                              min_delta=0,
                              patience=5,
                              verbose=0, mode='auto')
model = create_model()
train_batches, valid_batches, test_batches = create_data()
model.fit_generator(train_batches, steps_per_epoch=train_batches.samples/train_batches.batch_size, validation_data=valid_batches, 
                    validation_steps=valid_batches.samples/valid_batches.batch_size, epochs=250, verbose=2, callbacks=[early, checkpoint])
labels, predictions = predict(model, test_batches)
print(accuracy_score(labels, predictions))
     
