# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image /Volumes/HDD/TFG/DeepFashion/Category\ and\ Attribute\ Prediction\ Benchmark/Img/img/2-in-1_Space_Dye_Athletic_Tank/img_00000001.jpg

# import the necessary packages
import numpy as np
import argparse
import imutils
import dlib
import cv2
import math
from lib import *

predictorPath = "../detection_data/shape_predictor_68_face_landmarks.dat"
imagePath = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/img/Sheer_Pleated-Front_Blouse/img_00000001.jpg"

image = cv2.imread(imagePath)
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# convert dlib's rectangle to a OpenCV-style bounding box
# [i.e., (x, y, w, h)], then draw the face bounding box
x = 72
y = 79
w = 232
h = 273
cv2.rectangle(image, (w, h), (x, y), (0, 255, 0), 2)
#cv2.rectangle(image, (x-w, y+h), (x + w, y + val), (0, 255, 255), 2)
#crop = image[y+h:y + h*7, x-w:x + w*2]

# show the face number
cv2.putText(image, "Face #{}".format(1), (x - 10, y - 10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

"""cv2.circle(image, (shape[36][0], shape[36][1]), 1, (0, 0, 255), -1)
cv2.circle(image, (shape[37][0], shape[37][1]), 1, (0, 0, 255), -1)
cv2.circle(image, (shape[38][0], shape[38][1]), 1, (0, 0, 255), -1)
cv2.circle(image, (shape[39][0], shape[39][1]), 1, (0, 0, 255), -1)
cv2.circle(image, (shape[40][0], shape[40][1]), 1, (0, 0, 255), -1)
cv2.circle(image, (shape[41][0], shape[41][1]), 1, (0, 0, 255), -1)"""

# show the output image with the face detections + facial landmarks
cv2.imshow("Output", image)
cv2.waitKey(0)
#cv2.imwrite("tets.png", crop)
    