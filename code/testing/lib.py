import numpy as np
import math

def check(left, right):
    max = 0
    min = 0
    if left > right:
        max = left
        min = right
    else:
        max = right
        min = left
    realMin = max - (max * 0.25)
    if min < realMin:
        return False
    else:
        return True

def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
 
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
 
	# return the list of (x, y)-coordinates
	return coords

def calc_euclidean_distance(coor1, coor2):
    a = (coor2[0] - coor1[0])**2
    b = (coor2[1] - coor1[1])**2
    return math.sqrt(a+b)

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