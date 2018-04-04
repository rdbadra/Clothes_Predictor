import os
import errno

trainPath = os.getcwd()+"/../../train_data.txt"
validPath = os.getcwd()+"/../../validation_data.txt"
testPath = os.getcwd()+"/../../test_data.txt"
comparePathToRead = os.getcwd()+"/../../DeepFashion/Anno/list_bbox.txt"

def getDictionaryForFile(path, header=False):
    dict = {}
    with open(path, "r") as file:
        line = file.readline()
        line = file.readline()
        if header:
            line = file.readline()
        while line:
            split = line.split()
            dict[split[0]] = []
            for i in range(1, len(split)):
                dict[split[0]].append(split[i])
            line = file.readline()
    return dict

def createCoordinatesFileFromFile():
    createCoordinatesFiles(trainPath, "train")
    createCoordinatesFiles(testPath, "test")
    createCoordinatesFiles(validPath, "valid")

def createCoordinatesFiles(path, type):
    count = 1
    bbox = getDictionaryForFile(comparePathToRead, header=False)
    with open(path, "r") as subsetFile:
        line = subsetFile.readline()
        line = subsetFile.readline()
        while line:
            split = line.split()
            array = bbox[split[0]]
            fileName = split[0].replace(".jpg", ".txt")
            fileName = fileName.replace("/", "+")
            if not os.path.exists(os.path.dirname(os.getcwd()+"/../../face-coordinates/"+type+"/"+split[2]+"/"+fileName)):
                try:
                    os.makedirs(os.path.dirname(os.getcwd()+"/../../face-coordinates/"+type+"/"+split[2]+"/"+fileName))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            with open(os.getcwd()+"/../../face-coordinates/"+type+"/"+split[2]+"/"+fileName, "w+") as file:
                file.write(array[0]+";"+array[1]+";"+array[2]+";"+array[3]+";\n")
                
            count += 1
            line = subsetFile.readline()
    print(type+" : "+str(count))
    print("finished")