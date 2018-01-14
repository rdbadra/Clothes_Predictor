# This file will return a dictionary with the number of times each category is repeated
import numpy as np
import random

def writeSubset(outputPath, subset):
    writefile = open(outputPath, "w")
    for line in subset:
        writefile.write(line)

def generateSubset(list):
    rand_smpl = [ list[i] for i in sorted(random.sample(xrange(len(list)), 5000)) ]
    return rand_smpl

def getDatasetFileInMemory():
    list_category_img_path = "/Volumes/HDD/TFG/list_category_img.txt"

    list = []
    with open(list_category_img_path, "r") as fp:
        line = fp.readline()
        count = 1
        while line:
            list.append(line)
            line = fp.readline()
    return list

outputPath1 = "/Volumes/HDD/TFG/subset1.txt"
outputPath2 = "/Volumes/HDD/TFG/subset2.txt"

dataset = getDatasetFileInMemory()

print len(dataset)

subset1 = generateSubset(dataset)
print len(subset1)
#subset2 = generateSubset(dataset)

writeSubset(outputPath1, subset1)
#writeSubset(outputPath2, subset2)







print "Finished"