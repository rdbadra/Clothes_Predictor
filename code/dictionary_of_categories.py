# This file will return a dictionary with the number of times each category is repeated
import numpy as np
import argparse
import math
import collections

outputPath = "/Volumes/HDD/TFG/list_category_img.txt"
# File with list of images 
list_category_img_path = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_category_img.txt"

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