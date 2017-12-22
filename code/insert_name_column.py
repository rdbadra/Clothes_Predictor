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

d = collections.OrderedDict(sorted(dict.items()))
        
print d



print "Finished"