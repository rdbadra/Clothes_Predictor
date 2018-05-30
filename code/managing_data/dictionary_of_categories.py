# This file will return a dictionary with the number of times each category is repeated
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

currentPath = os.getcwd()

"""
Create a dictionary with the categories as keys, and value the number of examples
"""

def getDictionaryWithCategories(list_category_img_path = currentPath+"/../../height_width.txt"):
    dict = {}
    with open(list_category_img_path, "r") as fp:
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        count = 1
        while line:
            if (list_category_img_path == currentPath+"/../../DeepFashionAnno/list_category_img.txt"):
                split = line.split()
            else:
                split = line.split()
            #print(split)
            if split[1] in dict.keys():
                dict[split[1]] += 1
            else:
                dict[split[1]] = 1
            line = fp.readline()
    return dict

"""
Create a dictionary with the categories as keys, and value the number of examples
"""
def getDictionaryWithCategoriesFromList(list):
    dict = {}
    for line in list:
        split = line.split()
        if split[1] in dict.keys():
            dict[split[1]] += 1
        else:
            dict[split[1]] = 1
    return dict

"""
Gets array of keys of a dictionary
"""
def getListOfKeys(dict):
    listOfKeys = []
    #print(dict.keys())
    for key in dict.keys():
        listOfKeys.append(int(key))
    listOfKeys.sort()
    return listOfKeys

"""
Prints the total number of examples of the dictionary
"""
def getTotalNumberOfValuesInDictionary(dict):
    listOfKeys = getListOfKeys(dict)
    total = 0
    for number in listOfKeys:
        total += dict[str(number)]
    return total

"""
Gets a new dictionary with those keys wich values are more than 5000 examples
"""
def getCategoriesWithBigData(dictionary, listOfKeys):
    newDictionary = {}
    for n in listOfKeys:
        if (dictionary[str(n)] >= 5000):
            newDictionary[str(n)] = dictionary[str(n)]
    return newDictionary

"""
Draw graph of dictionary
"""
def drawHistogram(listOfKeys, dictionary):
    x = listOfKeys
    y = [dictionary[str(i)] for i in listOfKeys]
    plt.bar(x, y)
    plt.title("Histogram of Clothes Categories")
    plt.xlabel("Categories")
    plt.ylabel("Quantities")
    plt.show()

"""dict = getDictionaryWithCategories(list_category_img_path="/Volumes/HDD/TFG/big_data_list_category_img.txt")

keys = getListOfKeys(dict)
print(keys)
drawHistogram(keys, dict)"""
def createFileWith5000ElementsPerClass():
    dictionaryOfFullData = getDictionaryWithCategories(list_category_img_path=currentPath+"/../../full_data.txt")
    frame = pd.read_csv(os.getcwd()+"/../../full_data.txt",  delim_whitespace=True,skiprows=0)
    frame_dictionary = {}
    train_dictionary = {}
    test_dictionary = {}
    validation_dictionary = {}
    print(dictionaryOfFullData)
    for key in dictionaryOfFullData.keys():
        tempFrame = frame.loc[frame["category_label"]==int(key)]
        if int(key) != 30:
            if len(tempFrame) > 5000:
                 frame_dictionary[key] = tempFrame.sample(n = 5000)
            else: 
                frame_dictionary[key] = tempFrame.sample(n = 5000)
        else:
            frame_dictionary[key] = tempFrame
        test_dictionary[key] = frame_dictionary[key][:int(len(frame_dictionary[key])*0.3)]
        validation_dictionary[key] = frame_dictionary[key][int(len(frame_dictionary[key])*0.3):int(len(frame_dictionary[key])*0.3)+int((len(frame_dictionary[key])*0.7)*0.3)]
        train_dictionary[key] = frame_dictionary[key][int(len(frame_dictionary[key])*0.3)+int((len(frame_dictionary[key])*0.7)*0.3):]
    return frame_dictionary, test_dictionary, validation_dictionary, train_dictionary

def concatFrames(frame, fileName):
    listOfFrames = []
    for key in frame.keys():
        listOfFrames.append(frame[key])
    result = pd.concat(listOfFrames)
    print(len(result))
    result.to_csv(currentPath+"/../../"+fileName, sep=" ", index=False)


def createDataForTrainingAndTesting():
    total, test, val, train = createFileWith5000ElementsPerClass()
    #print(len(frame["30"]))
    concatFrames(total, "total_data.txt")
    concatFrames(test, "test_data.txt")
    concatFrames(val, "validation_data.txt")
    concatFrames(train, "train_data.txt")
#file = pd.read_csv(currentPath+"/../../setForTraining.txt", delim_whitespace=True,skiprows=0)
#print(file.describe())