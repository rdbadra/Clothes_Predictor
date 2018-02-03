pathToRead = "/Volumes/HDD/TFG/subsets/subset1.txt"
comparePathToRead = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_bbox.txt"

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
                    fileName = split[0].replace("/", "-")
                    fileName = fileName.replace(".jpg", ".txt")
                    with open("../../face-coordinates/"+fileName, "w+") as file:
                        file.write(bboxSplit[1]+";"+bboxSplit[2]+";"+bboxSplit[3]+";"+bboxSplit[4]+";\n")
                        break
                else:
                    bboxLine = bboxFile.readline()
        line = subsetFile.readline()
        count += 1
        if count % 100 == 0:
            print("file : "+str(count)+"\n")

print("finished")
        