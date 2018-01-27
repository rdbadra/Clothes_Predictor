"""
Script to find what categories are in our final data
"""
import dictionary_of_categories as dc

def getDictionaryOfCategoryNames(list_category_cloth_path = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_category_cloth.txt"):
    readfile = open(list_category_cloth_path, "r")
    dictionary = {}
    line = readfile.readline()
    line = readfile.readline()
    line = readfile.readline()
    count = 1
    while line:
        split = line.split()
        dictionary[str(count)] = split[0]
        count +=1
        line = readfile.readline()
    return dictionary

def checkWhatCategoriesWeHaveInFinalDataset():
    categoriesDictionary = getDictionaryOfCategoryNames()
    datasetDictionary = dc.getDictionaryWithCategories(list_category_img_path="/Volumes/HDD/TFG/big_data_list_category_img.txt")
    for key in datasetDictionary.keys():
        print(str(key)+" : "+categoriesDictionary[str(key)])  

checkWhatCategoriesWeHaveInFinalDataset()




print("Finished")