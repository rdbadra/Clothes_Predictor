import os
import errno

pathToRead = os.getcwd()+"/../../train_data.txt"
comparePathToRead = os.getcwd()+"/../../DeepFashion/Anno/list_bbox.txt"

def getDictionaryForFile(path, header=True):
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

def createCoordinatesFileFromSubset():
    count = 1
    with open(pathToRead, "r") as subsetFile:
        line = subsetFile.readline()
        line = subsetFile.readline()
        line = subsetFile.readline()
        while line:
            split = line.split()
            with open(comparePathToRead, "r") as bboxFile:
                bboxLine = bboxFile.readline()
                bboxLine = bboxFile.readline()
                bboxLine = bboxFile.readline()
                while bboxLine:
                    bboxSplit = bboxLine.split()
                    if split[0] == bboxSplit[0]:
                        #fileName = split[0].replace("/", "-")
                        fileName = split[0].replace(".jpg", ".txt")
                        if not os.path.exists(os.path.dirname(os.getcwd()+"/../../face-coordinates/"+fileName)):
                            try:
                                os.makedirs(os.path.dirname(os.getcwd()+"/../../face-coordinates/"+fileName))
                            except OSError as exc: # Guard against race condition
                                if exc.errno != errno.EEXIST:
                                    raise
                        with open(os.getcwd()+"/../../face-coordinates/"+fileName, "w+") as file:
                            file.write(bboxSplit[1]+";"+bboxSplit[2]+";"+bboxSplit[3]+";"+bboxSplit[4]+";\n")
                            break
                    else:
                        bboxLine = bboxFile.readline()
            line = subsetFile.readline()
            count += 1
            if count % 100 == 0:
                print("file : "+str(count)+"\n")
    print(count)
    print("finished")

def createCoordinatesFileFromFile():
    count = 1
    bbox = getDictionaryForFile(comparePathToRead, header=True)
    with open(pathToRead, "r") as subsetFile:
        line = subsetFile.readline()
        line = subsetFile.readline()
        while line:
            split = line.split()
            array = bbox[split[0]]
            fileName = split[0].replace(".jpg", ".txt")
            if not os.path.exists(os.path.dirname(os.getcwd()+"/../../face-coordinates/"+fileName)):
                try:
                    os.makedirs(os.path.dirname(os.getcwd()+"/../../face-coordinates/"+fileName))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            with open(os.getcwd()+"/../../face-coordinates/"+fileName, "w+") as file:
                file.write(array[0]+";"+array[1]+";"+array[2]+";"+array[3]+";\n")
                
            count += 1
            if count % 100 == 0:
                print("file : "+str(count)+"\n")
            line = subsetFile.readline()
    print(count)
    print("finished")
        