import os
import errno
import cv2

mypath = "/Volumes/HDD/TFG/face-coordinates/"
cropPath = "/Volumes/HDD/TFG/crops/"

f = [os.path.join(r,file) for r,d,f in os.walk(mypath) for file in f if file.endswith(".txt")]

for textFile in f:
    imageFile = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/" + textFile.replace(mypath, "")
    imageFile = imageFile.replace('.txt', '.jpg')
    with open(textFile) as coordinatesFile:
        coordinatesText = coordinatesFile.readline()
        splitCoordinates = coordinatesText.split(';')
        image = cv2.imread(imageFile)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        x1 = int(splitCoordinates[0])
        y1 = int(splitCoordinates[1])
        x2 = int(splitCoordinates[2])
        y2 = int(splitCoordinates[3])
        crop = image[y1:y2, x1:x2]
        resized_crop = cv2.resize(crop, (200, 200))
        path = cropPath + textFile.replace(mypath, "")
        path = path.replace('.txt', '.jpg')
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        print(path)
        cv2.imwrite(path, resized_crop)
        #cv2.imshow("Output", resized_crop)
        #cv2.waitKey(0)

print("FINISHED")