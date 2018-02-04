import os
import cv2

mypath = "/Volumes/HDD/TFG/face-coordinates/"

f = [os.path.join(r,file) for r,d,f in os.walk(mypath) for file in f if file.endswith(".txt")]

for textFile in f:
    imageFile = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/" + textFile.replace(mypath, "")
    imageFile = imageFile.replace('.txt', '.jpg')
    with open(textFile) as coordinatesFile:
        coordinatesText = coordinatesFile.readline()
        splitCoordinates = coordinatesText.split(';')
        image = cv2.imread(imageFile)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(image, (int(splitCoordinates[0]), int(splitCoordinates[1])), (int(splitCoordinates[2]), int(splitCoordinates[3])), (0, 255, 0), 2)
        cv2.imshow("Output", image)
        cv2.waitKey(0)