# This file will add two columns to the file 
# One column will be the name of the type of cloth
# The other column is a number that represents whether it is upper, lower, or full-body
import numpy as np
import argparse
import math
import collections

outputPath = "/Volumes/HDD/TFG/list_category_img.txt"
# File with list of images 
list_category_img_path = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_category_img.txt"
# File with the names of the categories
list_category_cloth_path = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_category_cloth.txt"

writefile = open(outputPath, "w")
with open(list_category_img_path, "r") as fp:
    line = fp.readline()

    count = 1
    while line:
        if count >= 3:
            split = line.split()
            with open(list_category_cloth_path, "r") as cloth:
                clothLine = cloth.readline()
                clothLine = cloth.readline()
                clothLine = cloth.readline()
                clothCount = 3
                while clothLine:
                    clothSplit = clothLine.split()
                    if int(split[1])+2 == clothCount:
                        line = split[0] + "\t\t" + split[1] + "\t"+clothSplit[0]+"\t\t"+clothSplit[1]+"\n"
                        writefile.write(line)
                        #print clothSplit
                        #break
                    clothLine = cloth.readline()
                    clothCount += 1
        #if count == 5:
        #    break    
        #break
        line = fp.readline()
        count += 1
        



print "Finished"