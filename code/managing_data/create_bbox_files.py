import os
import errno

pathToRead = os.getcwd()+"/../../subsets/subset1.txt"
comparePathToRead = os.getcwd()+"/../../DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_bbox.txt"

with open(pathToRead, "r") as subsetFile:
    line = subsetFile.readline()
    line = subsetFile.readline()
    line = subsetFile.readline()
    count = 1
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
                    if not os.path.exists(os.path.dirname(os.getcwd()+"../../face-coordinates/"+fileName)):
                        try:
                            os.makedirs(os.path.dirname(os.getcwd()+"../../face-coordinates/"+fileName))
                        except OSError as exc: # Guard against race condition
                            if exc.errno != errno.EEXIST:
                                raise
                    with open(os.getcwd()+"../../face-coordinates/"+fileName, "w+") as file:
                        file.write(bboxSplit[1]+";"+bboxSplit[2]+";"+bboxSplit[3]+";"+bboxSplit[4]+";\n")
                        break
                else:
                    bboxLine = bboxFile.readline()
        line = subsetFile.readline()
        count += 1
        if count % 100 == 0:
            print("file : "+str(count)+"\n")

print("finished")
        