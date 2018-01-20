import random
import dictionary_of_categories as dc
import math

"""
Creates a file containing the elements of the list "subset"
"""

def writeSubset(outputPath, subset):
    writefile = open(outputPath, "w")
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
        
# Voy por aqui
def generateProportionalSubset(list, dictionary):
    proportions = generateProportionalDictionary(list, dictionary)
    keys = dc.getListOfKeys(proportions)
    listOfThisKey = []
    finalList = []
    for key in keys:
        for line in list:
            split = line.split()
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

def getDatasetFileInMemory(list_category_img_path = "/Volumes/HDD/TFG/list_category_img.txt"):

    list = []
    with open(list_category_img_path, "r") as fp:
        line = fp.readline()
        count = 1
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
    print(total)

"""
Creates a file with new subset from a dataset that contains only the categories of keys
"""

def generateSubsetFromKeys(dataset, keys):
    path = "/Volumes/HDD/TFG/big_data_list_category_img.txt"
    writefile = open(path, "w")
    for line in dataset:
        split = line.split()
        if int(split[1]) in keys:
            writefile.write(line)


"""
Creates a file with the biggest amounts of data per category
"""
def createBigDataFile():
    fullDataset = getDatasetFileInMemory()
    fullDict = dc.getDictionaryWithCategories()
    fullDictKeys = dc.getListOfKeys(fullDict)
    maxDict = dc.getCategoriesWithBigData(fullDict, fullDictKeys)
    maxDictKeys = dc.getListOfKeys(maxDict)
    generateSubsetFromKeys(fullDataset, maxDictKeys)

dataset = getDatasetFileInMemory(list_category_img_path = "/Volumes/HDD/TFG/big_data_list_category_img.txt")
dictionary = dc.getDictionaryWithCategoriesFromList(dataset)
#print(dictionary)
#proportional = generateProportionalDictionary(dataset, dictionary)
subset1 = generateProportionalSubset(dataset, dictionary)
subset2 = generateProportionalSubset(dataset, dictionary)
compareSubsets(subset1, subset2)

writeSubset("/Volumes/HDD/TFG/subset1.txt", subset1)
writeSubset("/Volumes/HDD/TFG/subset2.txt", subset2)




print("Finished")