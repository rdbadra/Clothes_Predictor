import numpy as np
import argparse
import imutils
import dlib
import cv2
import math
import lib

predictorPath = "../detection_data/shape_predictor_68_face_landmarks.dat"
imagePath = ""

count = 0
for i in xrange(1,64):
    print "doing loop "+str(i)
    if i < 10:
         imagePath = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/img/2-in-1_Space_Dye_Athletic_Tank/img_0000000"+str(i)+".jpg"   
    else:
        imagePath = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/img/2-in-1_Space_Dye_Athletic_Tank/img_000000"+str(i)+".jpg"
    
   
    writefile = open("../face-coordinates/face-img_"+str(i)+".txt", "w")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictorPath)

    # load the input image, resize it, and convert it to grayscale
    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # detect faces in the grayscale image
    rects = detector(gray, 1)
    



    #print rects

    numberOfFaces = 0

    for (b, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = lib.shape_to_np(shape)
        if lib.check(lib.calc_euclidean_distance(shape[36], shape[39]), lib.calc_euclidean_distance(shape[42], shape[45])):
            numberOfFaces += 1
            writefile.write(str(numberOfFaces)+";\n")
            (x, y, w, h) = lib.rect_to_bb(rect)
            writefile.write(str(x)+";"+str(y)+";"+str(w)+";"+str(h)+";\n")

    if numberOfFaces == 0:
        writefile.write(str(numberOfFaces)+";\n")
    writefile.close()
    count = 0

print "Finished"