# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /Volumes/HDD/TFG/DeepFashion/Category\ and\ Attribute\ Prediction\ Benchmark/Img/img/2-in-1_Space_Dye_Athletic_Tank/img_00000001.jpg

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
 
# construct the argument parser and parse the arguments
"""ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to shape predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to image")
args = vars(ap.parse_args())
"""
predictorPath = "detection_data/shape_predictor_68_face_landmarks.dat"
imagePath = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/img/2-in-1_Space_Dye_Athletic_Tank/img_00000006.jpg"


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictorPath)

# load the input image, resize it, and convert it to grayscale
image = cv2.imread(imagePath)
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# detect faces in the grayscale image
rects = detector(gray, 1)

# loop over the face detections
file = open("face-coordinates/face-img_6.txt")
line = file.readline()
split = line.split(";")
num = int(split[0])
if(num > 0):
    line = file.readline()
    split = line.split(";")
    crop = []
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        x = int(split[0])
        y = int(split[1])
        w = int(split[2])
        h = int(split[3])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(image, (x-w, y+h), (x + w*2, y + h*7), (0, 255, 0), 2)
        crop = image[y+h:y + h*7, x-w:x + w*2]

        # show the face number
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # show the output image with the face detections + facial landmarks
    cv2.imshow("Output", image)
    cv2.waitKey(0)
    #cv2.imwrite("tets.png", crop)