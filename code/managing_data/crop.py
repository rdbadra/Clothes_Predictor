import os
import errno
import cv2

def cropImages():
    mypath = os.getcwd()+"/../../face-coordinates/"
    cropPath = os.getcwd()+"/../../crops/"
    count = 0
    f = [os.path.join(r,file) for r,d,f in os.walk(mypath) for file in f if file.endswith(".txt")]
    print("Total of "+str(len(f))+" files")
    for textFile in f:
        imageFile = textFile.replace(mypath, "")
        datapath = imageFile[:(imageFile.index("/")+1)]
        imageFile = imageFile[(imageFile.index("/")+1):]
        datapath += imageFile[:(imageFile.index("/")+1)]
        imageFile = imageFile[(imageFile.index("/")+1):]
        imageFile = os.getcwd()+"/../../DeepFashion/Img/" + imageFile
        imageFile = imageFile.replace('.txt', '.jpg')
        imageFile = imageFile.replace('+', '/')
        with open(textFile) as coordinatesFile:
            coordinatesText = coordinatesFile.readline()
            splitCoordinates = coordinatesText.split(';')
            image = cv2.imread(imageFile)
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            x1 = int(splitCoordinates[0])
            y1 = int(splitCoordinates[1])
            x2 = int(splitCoordinates[2])
            y2 = int(splitCoordinates[3])
            crop = image[y1:y2, x1:x2]
            resized_crop = cv2.resize(crop, (150, 200))
            path = cropPath + textFile.replace(mypath, "")
            path = path.replace('.txt', '.jpg')
            if not os.path.exists(os.path.dirname(path)):
                try:
                    os.makedirs(os.path.dirname(path))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            #print(path)
            cv2.imwrite(path, resized_crop)
            #cv2.imshow("Output", resized_crop)
            #cv2.waitKey(0)
        count +=1
    print(count)
    print("FINISHED CROPPING IMAGES")