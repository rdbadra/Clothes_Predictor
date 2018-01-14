import random

def writeSubset(outputPath, subset):
    writefile = open(outputPath, "w")
    for line in subset:
        writefile.write(line)

def generateSubset(list):
    random.shuffle(list)
    rand_smpl = [ list[i] for i in sorted(random.sample(range(len(list)), 5000)) ]
    return rand_smpl

def getDatasetFileInMemory():
    list_category_img_path = "/Volumes/HDD/TFG/list_category_img.txt"

    list = []
    with open(list_category_img_path, "r") as fp:
        line = fp.readline()
        count = 1
        while line:
            list.append(line)
            line = fp.readline()
    return list

def compareSubsets(s1, s2):
    total = 0
    for el1 in s1:
        for el2 in s2:
            if el2 == el1:
                total += 1
    print(total)

outputPath1 = "/Volumes/HDD/TFG/subset1.txt"
outputPath2 = "/Volumes/HDD/TFG/subset2.txt"

dataset = getDatasetFileInMemory()

print("Length if dataset %d" % len(dataset))

subset1 = generateSubset(dataset)
print("Length of subset %d" % len(subset1))
subset2 = generateSubset(dataset)

compareSubsets(subset1, subset2)

writeSubset(outputPath1, subset1)
writeSubset(outputPath2, subset2)







print("Finished")