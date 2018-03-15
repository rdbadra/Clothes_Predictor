import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import os

big_data = os.getcwd()+"/../../big_data_list_category_img.txt"
full_data = os.getcwd()+"/../../full_data.txt"
bbox_data = os.getcwd()+"/../../DeepFashion/Anno/list_bbox.txt"
file_with_sizes = os.getcwd()+"/../../height_width.txt"

def loadFile(path):
    list = []
    with open(path, "r") as file:
        line = file.readline()
        line = file.readline()
        line = file.readline()
        while line:
            list.append(line)
            line = file.readline()
    return list

def getDictionaryForFile(path, header=True):
    dict = {}
    with open(path, "r") as file:
        line = file.readline()
        line = file.readline()
        if header:
            line = file.readline()
        while line:
            split = line.split()
            dict[split[0]] = []
            for i in range(1, len(split)):
                dict[split[0]].append(split[i])
            line = file.readline()
    return dict

#getDictionaryForFile(os.getcwd()+"/../../list_category_img.txt")
def createSizeFile():
    dict = getDictionaryForFile(bbox_data)
    fileToCreate = open(file_with_sizes, "w")
    fileToCreate.write(str(len(dict))+"\n")
    fileToCreate.write("image_name  category_label  type_of_cloth  body_part  height  width  height/width_relation\n")
    with open(os.getcwd()+"/../../list_category_img.txt", "r") as file:
        line = file.readline()
        line = file.readline()
        line = file.readline()
        while line:
            split = line.split()
            array = dict[split[0]]
            x1 = array[0]
            y1 = array[1]
            x2 = array[2]
            y2 = array[3]
            width = int(x2)-int(x1)
            height = int(y2)-int(y1)
            relation = height/width
            line = split[0] + " " + split[1] + " " + split[2] + " " + split[3] + " " + str(height) +" " + str(width) + " " + str(relation) + "\n"
            fileToCreate.write(line)
            line = file.readline()

def getStandardDeviationAndVariance():
    heights = []
    widths = []
    with open(file_with_sizes, "r") as file:
        line = file.readline()
        line = file.readline()
        line = file.readline()
        while line:
            split = line.split("  ")
            widths.append(int(split[4]))
            heights.append(int(split[5]))
            line = file.readline()
    np_widths = np.array(widths)
    np_heights = np.array(heights)
    print("Std of widths: "+str(np.std(np_widths)))
    print("Var of widths: "+str(np.var(np_widths)))
    print("Std of heights: "+str(np.std(np_heights)))
    print("Var of heights: "+str(np.var(np_heights)))

def drawHeightsHistogram():
    dict = {}
    file = loadFile(file_with_sizes)
    for line in file:
        split = line.split()
        if split[1] in dict.keys():
            dict[split[1]].append(int(split[4]))
        else:
            dict[split[1]] = [int(split[4])]
    for key in dict.keys():
        plt.title(key)
        plt.hist(dict[key])
        plt.show()
        plt.clf()
#getStandardDeviationAndVariance()
#df = pd.read_csv("test.txt", delim_whitespace=True,skiprows=0)
#print(df.describe())
#category_label = df.loc[df['image_name'] == "img/Sheer_Pleated-Front_Blouse/img_00000001.jpg"].iloc[0][1]
#print(type(int(category_label)))
def eliminateCategoriesWithSmallBBox():
    df = pd.read_csv(big_data, delim_whitespace=True,skiprows=0,header=1)
    heightDF = df[df['height'] > 50]
    w = heightDF[heightDF["width"] > 50]
    #print(w.describe())
    w.to_csv(full_data, sep=" ", index=False)
df = pd.read_csv(full_data, delim_whitespace=True,skiprows=0)
print(df.describe())
#drawHeightsHistogram()
