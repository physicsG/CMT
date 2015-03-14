#!/usr/bin/env python

import argparse
import cv2
from numpy import empty, nan
import os
import sys
import time

import CMT
import numpy
import util

CMT = CMT.CMT()

pause_time = 10

# Oopen camera device
cap = cv2.VideoCapture(1)

# Check if videocapture is working
if not cap.isOpened():
	print 'Unable to open video input.'
	sys.exit(1)

window_main = "Main"
window_user_options = "User Options"
cv2.namedWindow(window_main,cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow(window_user_options,cv2.CV_WINDOW_AUTOSIZE)
cv2.moveWindow(window_main,960,0)
cv2.moveWindow(window_user_options,720,0)

frame = 1
line_thickness = 2
object_tracking = False
draw_box = False

while True:
	# Read image
	status, im = cap.read()
	if not status:
		break
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im_draw = numpy.copy(im_gray)
	
	im_user_options = numpy.zeros((480,240))
	
	if object_tracking:
		# Get rectangle input from user
		if draw_box:
			(tl, br) = util.get_rect(im_draw)
			CMT.initialise(im_gray, tl, br)
			draw_box = False

		tic = time.time()
		CMT.process_frame(im_gray)
		toc = time.time()
		
		# Display results
		
		# Draw updated estimate
		if CMT.has_result:
			
			crossHor = ((int(CMT.center[0])-10,int(CMT.center[1])),(int(CMT.center[0])+10,int(CMT.center[1])))
			crossVer = ((int(CMT.center[0]),int(CMT.center[1])-10),(int(CMT.center[0]),int(CMT.center[1])+10))
			
			cv2.line(im_draw, CMT.tl, CMT.tr, (255, 0, 0), line_thickness)
			cv2.line(im_draw, CMT.tr, CMT.br, (255, 0, 0), line_thickness)
			cv2.line(im_draw, CMT.br, CMT.bl, (255, 0, 0), line_thickness)
			cv2.line(im_draw, CMT.bl, CMT.tl, (255, 0, 0), line_thickness)
			cv2.line(im_draw, crossHor[0], crossHor[1], (0, 0, 0), 2)
			cv2.line(im_draw, crossVer[0], crossVer[1], (0, 0, 0), 2)

		util.draw_keypoints(CMT.tracked_keypoints, im_draw, (255, 255, 255))
		# this is from simplescale
		util.draw_keypoints(CMT.votes[:, :2], im_draw)  # blue
		util.draw_keypoints(CMT.outliers[:, :2], im_draw, (0, 0, 255))
		
		parameters = str('{5:04d}: center: {0:.2f},{1:.2f} scale: {2:.2f}, active: {3:03d}, {4:04.0f}ms'.format(CMT.center[0], CMT.center[1], CMT.scale_estimate, CMT.active_keypoints.shape[0], 1000 * (toc - tic), frame))
		
		cv2.putText(im_draw,parameters,(5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255))
		
		# Remember image
		im_prev = im_gray
		
		# Advance frame number
		frame += 1

	cv2.putText(im_user_options,"[Q] Quit", (5, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (1))
	cv2.putText(im_user_options,"[T] Object tracking: "+str(object_tracking), (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (1))
	cv2.putText(im_user_options,"[B] Draw new box", (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (1))

	cv2.imshow(window_main, im_draw)
	cv2.imshow(window_user_options,im_user_options)
	
	# Check key input
	k = cv2.waitKey(pause_time)
	
	if k != -1:
		key = chr(k & 255)
		if key == 't':
			object_tracking = not object_tracking
			draw_box = not draw_box
		
		if key == 'b':
			draw_box = True
		
		if key == 'q':
			break



	
