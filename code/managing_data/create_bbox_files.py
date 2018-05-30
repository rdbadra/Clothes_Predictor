import os
import errno

trainPath = os.getcwd()+"/../../train_data.txt"
validPath = os.getcwd()+"/../../validation_data.txt"
testPath = os.getcwd()+"/../../test_data.txt"
comparePathToRead = os.getcwd()+"/../../DeepFashion/Anno/list_bbox.txt"

name_of_file = 'face-coordinates/'

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

def createCoordinatesFileFromFile(fullbody=False):
    createCoordinatesFiles(trainPath, "train", body=fullbody)
    createCoordinatesFiles(testPath, "test", body=fullbody)
    createCoordinatesFiles(validPath, "valid", body=fullbody)

def convertToBodyPart(num):
    if int(num) is 1:
        return 'upper-body'
    elif int(num) is 2:
        return 'lower-body'
    else:
        return 'full-body'

def createCoordinatesFiles(path, type, body=False):
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
            if body is True:
                if not os.path.exists(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+convertToBodyPart(split[3])+"/"+fileName)):
                    try:
                        os.makedirs(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+convertToBodyPart(split[3])+"/"+fileName))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(os.getcwd()+"/../../"+name_of_file+type+"/"+convertToBodyPart(split[3])+"/"+fileName, "w+") as file:
                    file.write(array[0]+";"+array[1]+";"+array[2]+";"+array[3]+";\n")
            else:
                # if split[2] == 'Cardigan' or split[2] == 'Jacket' or split[2] == 'Blazer':
                #     if not os.path.exists(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+"Jacket-Blazer-Cardigan"+"/"+fileName)):
                #         try:
                #             os.makedirs(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+"Jacket-Blazer-Cardigan"+"/"+fileName))
                #         except OSError as exc: # Guard against race condition
                #             if exc.errno != errno.EEXIST:
                #                 raise
                #     with open(os.getcwd()+"/../../"+name_of_file+type+"/"+"Jacket-Blazer-Cardigan"+"/"+fileName, "w+") as file:
                #         file.write(array[0]+";"+array[1]+";"+array[2]+";"+array[3]+";\n")

                # elif split[2] == 'Tank' or split[2] == 'Blouse' or split[2] == 'Tee' or split[2] == 'Top':
                #     if not os.path.exists(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+"Blouse-Tank-Tee-Top"+"/"+fileName)):
                #         try:
                #             os.makedirs(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+"Blouse-Tank-Tee-Top"+"/"+fileName))
                #         except OSError as exc: # Guard against race condition
                #             if exc.errno != errno.EEXIST:
                #                 raise
                #     with open(os.getcwd()+"/../../"+name_of_file+type+"/"+"Blouse-Tank-Tee-Top"+"/"+fileName, "w+") as file:
                #         file.write(array[0]+";"+array[1]+";"+array[2]+";"+array[3]+";\n")

                # else:
                if not os.path.exists(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+split[2]+"/"+fileName)):
                    try:
                        os.makedirs(os.path.dirname(os.getcwd()+"/../../"+name_of_file+type+"/"+split[2]+"/"+fileName))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(os.getcwd()+"/../../"+name_of_file+type+"/"+split[2]+"/"+fileName, "w+") as file:
                    file.write(array[0]+";"+array[1]+";"+array[2]+";"+array[3]+";\n")
                
            count += 1
            line = subsetFile.readline()
    print(type+" : "+str(count))
    print("finished creating coordinates files")