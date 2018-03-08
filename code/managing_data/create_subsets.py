import random
import dictionary_of_categories as dc
import math
import os

"""
Creates a file containing the elements of the list "subset"
"""
def writeSubset(outputPath, subset):
    dictionary = dc.getDictionaryWithCategoriesFromList(subset)
    total = dc.getTotalNumberOfValuesInDictionary(dictionary)
    writefile = open(outputPath, "w")
    writefile.write(str(total)+"\n")
    writefile.write("image_name"+" "+"category_label"+" "+"type_of_cloth"+" "+"body_part"+" "+"height"+" "+"width"+" "+"height/width_relation"+"\n")
    for line in subset:
        writefile.write(line)

"""
Generates a new random list of 5000 examples
"""
def generateSubset(list):
    #random.shuffle(list)
    rand_smpl = [ list[i] for i in sorted(random.sample(range(len(list)), 5000)) ]
    return rand_smpl

"""
Creates a new dictionary with the proportional values to 5000 elements
"""
def generateProportionalDictionary(list, dictionary):
    total = dc.getTotalNumberOfValuesInDictionary(dictionary)
    keys = dc.getListOfKeys(dictionary)
    proportions = {}
    for key in keys:
        proportions[str(key)] = math.ceil((dictionary[str(key)]/total)*5000)
    return proportions
        
"""
Creates a list with the proportional values to 5000 elements
"""
def generateProportionalSubset(list, dictionary):
    proportions = generateProportionalDictionary(list, dictionary)
    keys = dc.getListOfKeys(proportions)
    listOfThisKey = []
    finalList = []
    for key in keys:
        for line in list:
            split = line.split(' ')
            if(int(split[1]) == key):
                listOfThisKey.append(line)
        reducedList = [ listOfThisKey[i] for i in sorted(random.sample(range(len(listOfThisKey)), proportions[str(key)])) ]
        for element in reducedList:
            finalList.append(element)
        reducedList = []
        listOfThisKey = []
    finalList = [ finalList[i] for i in sorted(random.sample(range(len(finalList)), 5000)) ]
    return finalList

"""
Creates a list containing all elements of a file
"""
def getDatasetFileInMemory(list_category_img_path = os.getcwd()+"/../../list_category_img.txt"):

    list = []
    with open(list_category_img_path, "r") as fp:
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        while line:
            list.append(line)
            line = fp.readline()
    return list

"""
Compares how many elements are repeated between two subsets
"""
def compareSubsets(s1, s2):
    total = 0
    for el1 in s1:
        for el2 in s2:
            if el2 == el1:
                total += 1
    print("Number of repeated Elements: "+str(total))

"""
Creates a file with new subset from a dataset that contains only the categories of keys
Here we also join categories 17 and 19 into 19
"""
def generateSubsetFromKeys(dataset, dictionary, keys):
    path =os.getcwd()+"/../../big_data_list_category_img.txt"
    writefile = open(path, "w")
    total = dc.getTotalNumberOfValuesInDictionary(dictionary)
    writefile.write(str(total)+"\n")
    writefile.write("image_name"+"  "+"category_label"+"  "+"type_of_cloth"+"  "+"body_part"+"\n")
    for line in dataset:
        split = line.split()
        #print(split)
        if int(split[1]) in keys:
            if int(split[1]) is 17:
                writefile.write(split[0]+"  "+str(19)+"  "+split[2]+"  "+split[3]+"\n")
            else:
                writefile.write(split[0]+"  "+split[1]+"  "+split[2]+"  "+split[3]+"\n")


"""
Creates a file with the biggest amounts of data per category
"""
def createBigDataFile():
    fullDataset = getDatasetFileInMemory()
    fullDict = dc.getDictionaryWithCategories()
    fullDictKeys = dc.getListOfKeys(fullDict)
    maxDict = dc.getCategoriesWithBigData(fullDict, fullDictKeys)
    maxDictKeys = dc.getListOfKeys(maxDict)
    generateSubsetFromKeys(fullDataset, maxDict, maxDictKeys)

#createBigDataFile()
dic=dc.getDictionaryWithCategories(os.getcwd()+"/../../full_data.txt")
print(dic)
print("Total Values in Dictionary Big Data : "+str(dc.getTotalNumberOfValuesInDictionary(dic)))
"""dataset = getDatasetFileInMemory(list_category_img_path = os.getcwd()+"/../../full_data.txt")
dictionary = dc.getDictionaryWithCategoriesFromList(dataset)
subset1 = generateProportionalSubset(dataset, dictionary)
subset2 = generateProportionalSubset(dataset, dictionary)
subset3 = generateProportionalSubset(dataset, dictionary)
compareSubsets(subset1, subset2)

writeSubset(os.getcwd()+"/../../subset1.txt", subset1)
writeSubset(os.getcwd()+"/../../subset2.txt", subset2)
writeSubset(os.getcwd()+"/../../subset3.txt", subset3)
dic=dc.getDictionaryWithCategories(os.getcwd()+"/../../subset1.txt")
print("Subset 1: ")
print(dic)
print(dc.getTotalNumberOfValuesInDictionary(dic))
dic=dc.getDictionaryWithCategories(os.getcwd()+"/../../subset2.txt")
print("Subset 2: ")
print(dic)
print(dc.getTotalNumberOfValuesInDictionary(dic))
dic=dc.getDictionaryWithCategories(os.getcwd()+"/../../subset3.txt")
print("Subset 3: ")
print(dic)
print(dc.getTotalNumberOfValuesInDictionary(dic))
print("Finished")"""