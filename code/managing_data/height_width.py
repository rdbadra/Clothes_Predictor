import numpy as np
import pandas as pd
import time

big_data = "/Volumes/HDD/TFG/big_data_list_category_img.txt"
full_data = "/Volumes/HDD/TFG/height_width.txt"
bbox_data = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_bbox.txt"
file_with_sizes = "/Volumes/HDD/TFG/height_width.txt"

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
    fileToCreate = open(file_with_sizes, "w")
    with open(big_data, "r") as big_data_file:
        big_line = big_data_file.readline()
        fileToCreate.write(big_line)
        fileToCreate.write("image_name;height,width;height/width_relation\n")
        big_line = big_data_file.readline()
        big_line = big_data_file.readline()
        index = 1
        while big_line:
            big_split = big_line.split()
            with open(bbox_data, "r") as bbox_data_file:
                bbox_line = bbox_data_file.readline()
                bbox_line = bbox_data_file.readline()
                bbox_line = bbox_data_file.readline()
                while bbox_line:
                    bbox_split = bbox_line.split()
                    if (bbox_split[0] == big_split[0]):
                        width = int(bbox_split[3]) - int(bbox_split[1])
                        height = int(bbox_split[4]) - int(bbox_split[2])
                        relation = height/width
                        fileToCreate.write(bbox_split[0] + ";" + str(width) + ";" + 
                        str(height) + ";" + str(relation) + ";\n")
                        break
                    bbox_line = bbox_data_file.readline()
                bbox_line = bbox_data_file.readline()
            if (index % 100) == 0:
                print(index)
            index += 1
            big_line = big_data_file.readline()
    print("finished")

def createSizeFile2():
    big = loadFile(big_data)
    bbox = loadFile(bbox_data)
    fileToCreate = open(file_with_sizes, "w")
    fileToCreate.write(str(len(big))+"\n")
    fileToCreate.write("image_name  category_label  type_of_cloth  body_part  height  width  height/width_relation\n")
    i = 0
    for big_line in big:
        big_split = big_line.split(',')
        if (i % 10000) == 0:
            print(i)
        i += 1
        bef = time.time()
        for bbox_line in bbox:
            bbox_split = bbox_line.split()
            if(big_split[0] == bbox_split[0]):
                width = int(bbox_split[3]) - int(bbox_split[1])
                height = int(bbox_split[4]) - int(bbox_split[2])
                relation = height/width
                fileToCreate.write(big_split[0]+"  "+big_split[1]+"  "+big_split[2]+"  "+
                big_split[3]+"  "+bbox_split[0] + "  " + str(width) + "  " + 
                str(height) + "  " + str(relation) + "\n")
                break
        now = time.time()
        print(str(1000*(now-bef))+"ms")
    print("finished")

def createSizeFile3():
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
            split = line.split(";")
            widths.append(int(split[1]))
            heights.append(int(split[2]))
            line = file.readline()
    np_widths = np.array(widths)
    np_heights = np.array(heights)
    print("Std of widths: "+str(np.std(np_widths)))
    print("Var of widths: "+str(np.var(np_widths)))
    print("Std of heights: "+str(np.std(np_heights)))
    print("Var of heights: "+str(np.var(np_heights)))
#createSizeFile3()
#getStandardDeviationAndVariance()
#df = pd.read_csv(bbox_data, delim_whitespace=True,skiprows=0,header=1)
#category_label = df.loc[df['image_name'] == "img/Sheer_Pleated-Front_Blouse/img_00000001.jpg"].iloc[0][1]
#print(type(int(category_label)))

df = pd.read_csv(full_data, delim_whitespace=True,skiprows=0,header=1)
print(df.describe())
