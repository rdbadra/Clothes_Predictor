# This file will return a dictionary with the number of times each category is repeated
import numpy as np
import matplotlib.pyplot as plt

"""
Create a dictionary with the categories as keys, and value the number of examples
"""

def getDictionaryWithCategories(list_category_img_path = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_category_img.txt"):
    dict = {}
    with open(list_category_img_path, "r") as fp:
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        count = 1
        while line:
            split = line.split()
            if split[1] in dict.keys():
                dict[split[1]] += 1
            else:
                dict[split[1]] = 1
            line = fp.readline()
    return dict

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