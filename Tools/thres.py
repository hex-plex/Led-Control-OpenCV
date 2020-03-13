import cv2
import numpy as np
cam=cv2.VideoCapture(0)
lowerskin=np.array([0,11,145])
upperskin=np.array([179, 46, 255 ])
while True:
	fram=cam.read()[1]
	cv2.imshow("fram",fram)
	fram=cv2.cvtColor(fram,cv2.COLOR_BGR2HSV)
	frame = cv2.GaussianBlur(cv2.resize(fram,tuple([320,240]),interpolation=cv2.INTER_AREA),(9,9),0)
	a=cv2.inRange(frame,lowerskin,upperskin)
	kernel=np.ones((7,7),np.uint8)
	a=cv2.dilate(a ,kernel )
	cv2.imshow("frame",a)
	if cv2.waitKey(1) & ord("q")==0xFF:
		break

cam.release()
