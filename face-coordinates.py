import numpy as np
import argparse
import imutils
import dlib
import cv2

def rect_to_bb(rect):
	# take a bounding predicted by dlib and convert it
	# to the format (x, y, w, h) as we would normally do
	# with OpenCV
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
 
	# return a tuple of (x, y, w, h)
	return (x, y, w, h)

predictorPath = "shape_predictor_68_face_landmarks.dat"
imagePath = ""

count = 0
for i in xrange(1,64):
    print "doing loop "+str(i)
    if i < 10:
         imagePath = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/img/2-in-1_Space_Dye_Athletic_Tank/img_0000000"+str(i)+".jpg"   
    else:
        imagePath = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/img/2-in-1_Space_Dye_Athletic_Tank/img_000000"+str(i)+".jpg"
    
   
    writefile = open("face-coordinates/face-img_"+str(i)+".txt", "w")
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
        numberOfFaces += 1

    writefile.write(str(numberOfFaces)+";\n")



    for (b, rect) in enumerate(rects):

        (x, y, w, h) = rect_to_bb(rect)
        writefile.write(str(x)+";"+str(y)+";"+str(w)+";"+str(h)+";\n")
    writefile.close()
    count = 0

print "Finished"

def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
 
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
 
	# return the list of (x, y)-coordinates
	return coords