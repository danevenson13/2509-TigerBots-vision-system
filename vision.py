import cv2
import numpy as np
import matplotlib.pyplot as plt 
radius = 7
red = [85.0, 118.0]
green = [69.0, 255.0]
blue = [0.0, 255.0]
width = 320.0
height = 240.0
interpolation = cv2.INTER_CUBIC
min_area = 0
min_perimeter = 0
min_width = 2
max_width = 1000
min_height = 7
max_height = 1000
solidity = [53, 65]
max_vertex_count = 20
min_vertex_count = 10
min_ratio = 1
max_ratio = 1000.0 
NUM_cont = 0

asasdasd = cv2.imread("\\Users\\User\\Desktop\\FRC images\\WIN_20170225_13_48_34_Pro.jpg")
asasdas = cv2.imread("\\Users\\User\\Desktop\\FRC images\\WIN_20170225_13_43_34_Pro.jpg")
"""image of boiler"""
img1 = cv2.resize(asasdasd, ((int)(width), (int)(height)), 0, 0, interpolation)
img2 = cv2.resize(asasdasd, ((int)(width), (int)(height)), 0, 0, interpolation) 
img3 = cv2.resize(asasdasd, ((int)(width), (int)(height)), 0, 0, interpolation) 
"""Resize image vaulues"""

"""shows itial image"""	               


	
	











RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
"""converts BGR(The color cv2 pulls out) to RGB""" 
cv2.imshow('gray', RGB) 
thresh = cv2.inRange(RGB, (red[0], green[0], blue[0]),  (red[1], green[1], blue[1]))
"""Thresholds the image with the RGB values set above"""
TARGET_LIGHT = cv2.inRange(RGB, (248, 248, 248),  (255, 255, 255))
"""Threshhold to extract boiuler target and White light"""
TARGET = cv2.inRange(RGB, (251, 253, 251),  (253, 255, 251))
"""thresholds out just the lights"""
ksize = int(2 * round(radius) + 1)
"""creates a kernel used for blurring in the net step"""
BLUR_TARGET = cv2.medianBlur(TARGET, ksize)
"""Blur used to get riqd of particles of the target in the Target threshold""" 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
"""creates a rectaular kernal for the operation next"""
dilation = cv2.dilate(BLUR_TARGET,kernel,iterations = 4)
"""becase of the blur lights are smaller than then there orginal this dilates the image"""

FINAL = cv2.subtract(TARGET_LIGHT, dilation)

mask = cv2.subtract(TARGET_LIGHT, dilation)
"""subtracts the image with the lights and the one with both target and light essentially filter the lights this will only work wiht the shop lights but a proof of concept"""
mode = cv2.RETR_LIST
method = cv2.CHAIN_APPROX_SIMPLE
cv2.imshow('asdasd', FINAL)

im2, contours1, hierarchy = cv2.findContours(FINAL, mode, method)
c2 = cv2.drawContours(img1, contours1, -1, (0,255,0), 10) 
cv2.imshow('img', c2) 
mean_val = cv2.mean(img2, mask = mask) 
print (mean_val)


"""draws the contours on the orginal image for displaying"""

output = []

for contour in contours1:
	
	x,y,w,h = cv2.boundingRect(contour)
	area = cv2.contourArea(contour)
	hull = cv2.convexHull(contour)
	dia = np.sqrt(4*area/np.pi)
	hull_area = cv2.contourArea(hull)


	print (dia)
	print (len(contour))
	if (len(contour) < 7 and len(contour) > 0):
		
		continue
	ratio = (float)(w) / h
	
	if (ratio < 1000 and ratio > 0.9):
		output.append(contour)
		Filter = cv2.drawContours(img2, output, 0, (0,255,0), 10)
		print ('asdasdasda %s' % output[0])
		cv2.imshow("len(output)", Filter)
		
		continue
	"""these actions filter our contours.  If they pass all the checks we then add them to the output list"""
	
	"""draws the filterd contours on the orginal image"""


			
while True:		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		print (len(output))
		print (len(contours1))
		"""prints the number contours and realeases the camerea if using a webcam"""
		cv2.imshow('THIS MIGHT WORK', c2)
		print (asdasdasdas)
