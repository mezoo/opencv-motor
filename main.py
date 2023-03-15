import cv2 as cv
import numpy as np

#cap = cv.VideoCapture('v4l2src device=/dev/video0 ! image/jpeg,width=640,height=480,framerate=30/1,format=(string)MJPG ! jpegdec ! appsink', cv.CAP_GSTREAMER)
#cap = cv.VideoCapture("videotestsrc ! appsink")
#cap = cv.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw,width=640,height=480,framerate=30/1,format=YUY2 ! videoconvert ! appsink", cv.CAP_GSTREAMER)
cap = cv.VideoCapture(0)
cv.getBuildInformation()

print()

if not cap.isOpened():
	print("Cannont open Camera")
	exit

while(True):
	ret, frame = cap.read()
	if ret == True:
		cv.imshow('Frame', frame)
		if cv.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv.destroyAllWindows()
