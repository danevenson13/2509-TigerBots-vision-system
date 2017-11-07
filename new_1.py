import cv2
import numpy as np
import matplotlib.pyplot as plt 
import math
import time
radius = 7
red = [85.0, 118.0]
green = [69.0, 255.0]
blue = [0.0, 255.0]
width = 640
height = 480
interpolation = cv2.INTER_CUBIC

NUM_cont = 0
hue = [33.99280575539568, 140.6060606060606]
sat = [139.88309352517985, 231.38888888888889]
lum = [91.72661870503596, 255.0]
asasdasd = cv2.imread("\\Users\\User\\Desktop\\FRC images\\WIN_20170225_13_43_34_Pro.jpg")
"""image of boiler"""
img1 = cv2.resize(asasdasd, ((int)(width), (int)(height)), 0, 0, interpolation)
img2 = cv2.resize(asasdasd, ((int)(width), (int)(height)), 0, 0, interpolation)

min_perimeter = 0
min_width = 0
max_width = 1000
min_height = 0
max_height = 1000
solidity = [138, 138.1]
max_vertices = 1000000
min_vertices = 0
min_ratio = 0.0
max_ratio = 1000

	
	











out = cv2.cvtColor(img1, cv2.COLOR_BGR2HLS)
thresh = cv2.inRange(out, (hue[0], lum[0], sat[0]),  (hue[1], lum[1], sat[1]))
cv2.imshow('asdasads', thresh)
"""subtracts the image with the lights and the one with both target and light essentially filter the lights this will only work wiht the shop lights but a proof of concept"""
mode = cv2.RETR_LIST
method = cv2.CHAIN_APPROX_SIMPLE
kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(thresh,kernel,iterations = 1)
cv2.imshow('asdasd', dilation)

im2, contours1, hierarchy = cv2.findContours(dilation, mode, method)
final = cv2.drawContours(img1, contours1, -1, (0,255,0), 2) 
cv2.imshow('finzczxczxcal', final)




"""draws the contours on the orginal image for displaying"""

output = []

for contour in contours1:
	
	x,y,w,h = cv2.boundingRect(contour)
	area = cv2.contourArea(contour)
	hull = cv2.convexHull(contour)
	area = w * h
	hull_area = cv2.contourArea(hull)
	hull = cv2.convexHull(contour)
	solid = 100 * area / cv2.contourArea(hull)
	area = cv2.contourArea(contour)
	
	if (solid > solidity[0] and solid < solidity[1]):
		output.append(contour)
		
		continue
	Filter = cv2.drawContours(img2, output, -1, (0,255,0), 2)
	cv2.imshow("len(output)", Filter)
	

	
		
	"""these actions filter our contours.  If they pass all the checks we then add them to the output list"""
	
	"""draws the filterd contours on the orginal image"""


cv2.imshow("len(output)", Filter)
for contour in output:
		
	x,y,w,h = cv2.boundingRect(contour)
	print (x)
	angle_to_target = math.atan((x-319.5)/554.25)
	angle_to_target_degrees = math.degrees(angle_to_target)
	print (angle_to_target_degrees)
	print (y)
	Vert_Angle = math.atan((y-239.5)/554.25)
	print (Vert_Angle)
	Distance_Angle = Vert_Angle+40
	c = math.tan(40)
	print (c)
	c_degrees = math.degrees(c)
	print (c_degrees)
	distance = 10/c_degrees
	print (distance)
	
	



			
while True:		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		'''print (len(output))
		print (len(contours1))
		"""prints the number contours and realeases the camerea if using a webcam"""
		cv2.imshow('THIS MIGHT WORK', c2)'''
		print (asdasdasdas)