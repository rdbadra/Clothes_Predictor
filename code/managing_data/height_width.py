import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import os

big_data = os.getcwd()+"/../../big_data_list_category_img.txt"
full_data = os.getcwd()+"/../../full_data.txt"
bbox_data = os.getcwd()+"/../../DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_bbox.txt"
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

def createSizeFile():
    big = loadFile(big_data)
    bbox = loadFile(bbox_data)
    df = pd.read_csv(bbox_data, delim_whitespace=True,skiprows=0,header=1)
    fileToCreate = open(file_with_sizes, "w")
    fileToCreate.write(str(len(big))+"\n")
    fileToCreate.write("image_name  category_label  type_of_cloth  body_part  height  width  height/width_relation\n")
    i = 0
    times = []
    
    for big_line in big:
        bef = time.time()
        big_split = big_line.split('  ')
        if (i % 1000) == 0:
            print(i)
        i += 1
        now = time.time()
        width = int(df.loc[df['image_name'] == big_split[0]].iloc[0][3]) - int(df.loc[df['image_name'] == big_split[0]].iloc[0][1])
        height = int(df.loc[df['image_name'] == big_split[0]].iloc[0][4]) - int(df.loc[df['image_name'] == big_split[0]].iloc[0][2])
        relation = height/width
        nextsplit = big_split[3].split("\n")
        #print(nextsplit)
        line = big_split[0]+"  "+big_split[1]+"  "+big_split[2]+"  "+nextsplit[0]+"  "+ str(height)+ "  " + str(width) + "  " + str(relation) + "\n"
        #print(line)
        fileToCreate.write(line)
        after = time.time()
        res = 1000*(after-now)
        times.append(res)
    np_times = np.array(times)
    print("Mean time taken per line: "+str(np.mean(np_times)))
    print("finished")

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
createSizeFile()
#getStandardDeviationAndVariance()
#df = pd.read_csv("test.txt", delim_whitespace=True,skiprows=0)
#print(df.describe())
#category_label = df.loc[df['image_name'] == "img/Sheer_Pleated-Front_Blouse/img_00000001.jpg"].iloc[0][1]
#print(type(int(category_label)))
df = pd.read_csv(full_data, delim_whitespace=True,skiprows=0,header=1)
print(df.head())
heightDF = df[df['height'] > 50]
w = heightDF[heightDF["width"] > 50]
#print(w.describe())
w.to_csv("full_data.txt", sep=" ", index=False)

#drawHeightsHistogram()
