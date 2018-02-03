import cv2

imagePath = "/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Img/img/Sheer_Pleated-Front_Blouse/img_00000006.jpg"

image = cv2.imread(imagePath)
#image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.rectangle(image, (47, 67), (211, 241), (0, 255, 0), 2)
cv2.imshow("Output", image)
cv2.waitKey(0)