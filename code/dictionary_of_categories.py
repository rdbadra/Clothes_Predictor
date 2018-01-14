# This file will return a dictionary with the number of times each category is repeated
import numpy as np
import matplotlib.pyplot as plt

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

def getListOfKeys(dict):
    listOfKeys = []
    for key in dict.keys():
        listOfKeys.append(int(key))
    listOfKeys.sort()
    return listOfKeys

def checkIfDictionaryIsCorrect():
    dict = getDictionaryWithCategories()
    listOfKeys = getListOfKeys(dict)
    total = 0
    for number in listOfKeys:
        total += dict[str(number)]
    print(total)

#checkIfDictionaryIsCorrect()

def drawHistogram(listOfKeys, dictionary):
    x = listOfKeys
    y = [dictionary[str(i)] for i in listOfKeys]
    plt.bar(x, y)
    plt.title("Histogram of Clothes Categories")
    plt.xlabel("Categories")
    plt.ylabel("Quantities")
    plt.show()

dict = getDictionaryWithCategories()
print(dict)
listOfKeys = getListOfKeys(dict)
drawHistogram(listOfKeys, dict)



print("Finished")