import numpy as np

big_data = "/Volumes/HDD/TFG/big_data_list_category_img.txt"
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
    fileToCreate.write("image_name;height,width;height/width_relation\n")
    i = 0
    for big_line in big:
        big_split = big_line.split()
        if (i % 10000) == 0:
            print(i)
        i += 1
        for bbox_line in bbox:
            bbox_split = bbox_line.split()
            if(big_split[0] == bbox_split[0]):
                width = int(bbox_split[3]) - int(bbox_split[1])
                height = int(bbox_split[4]) - int(bbox_split[2])
                relation = height/width
                fileToCreate.write(bbox_split[0] + ";" + str(width) + ";" + 
                str(height) + ";" + str(relation) + ";\n")
                break
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
#createSizeFile2()
#getStandardDeviationAndVariance()
import pandas as pd

df = pd.read_csv(big_data, sep='  ', header=1)
print(df.loc[df['type_of_cloth'] == 'Blouse'])