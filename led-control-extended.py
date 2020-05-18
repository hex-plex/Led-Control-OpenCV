import cv2
import numpy as  np
#import serial as sl
#import urllib2
import imutils
import pyautogui as pyg
import time

def dst(x1,y1,x0=0,y0=0):
	return (x1-x0)**2+(y1-y0)**2

cam=cv2.VideoCapture(0)
frame=cam.read()[1]
cv2.waitKey(1)
r=cv2.selectROI(frame)
frame=cv2.resize(frame,tuple([320,240]),interpolation=cv2.INTER_AREA)
y,x,_=(frame.shape)
print(y,x)
r=(x,y/2,b'r')
l=(0,y/2,b'l')
u=(x/2,0,b'u')
d=(x/2,y, b'd')
direc=[r,l,u,d]
#ser=sl.Serial('/dev/ttyACM0',38400)
#cv2.circle(frame,(d[0],d[1]),7,(255,0,0),-1)
#cv2.imshow('frame',frame)
#cv2.waitKey(0)
lowerskin=np.array([0,11,145])
upperskin=np.array([179, 46, 255 ])
flag=True
prevcenter=(-1,-1)
center=(-1,-1)
init=time.time()
while flag:
        fram=cam.read()[1]
        cv2.imshow("fram",fram)
        fram=cv2.resize(fram,tuple([320,240]),interpolation=cv2.INTER_AREA)
        frame = cv2.GaussianBlur(cv2.resize(fram,tuple([320,240]),interpolation=cv2.INTER_AREA),(9,9),0)
        framehsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        a=cv2.inRange(framehsv,lowerskin,upperskin)

        kernel=np.ones((7,7),np.uint8)
        a=cv2.dilate(a ,kernel )
        cv2.imshow("frme",a)

        contours=cv2.findContours(a,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnts=imutils.grab_contours(contours)
        max=0

        for c in cnts:
                epsilon = 0.0001*cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, epsilon, True)
                area=cv2.contourArea(c)
                if area>max:
                        hand=cv2.convexHull(c)
                        max=area
        cv2.drawContours(fram,[hand],-1,(0,255,0),3)
        M=cv2.moments(hand)
        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])
        center=(cx,cy)
        cv2.circle(fram,center,7,(255,0,0),-1)
        cv2.imshow("frame",fram)
        if prevcenter[0]>0 and prevcenter[1]>0:
                cutoff=dst(center[0],center[0],prevcenter[0],prevcenter[1])
                #print(cutoff)
                if cutoff>1000:
                        if abs(center[0]-prevcenter[0])>abs(center[1]-prevcenter[1]):
                                print(((center[0]-prevcenter[0])/(time.time()-init)))                                
                                if 175<abs((center[0]-prevcenter[0])/(time.time()-init))<300:
                                        #print(((center[0]-prevcenter[0])/(time.time()-init)))        
                                        if center[0]-prevcenter[0] > 0 :
                                                pyg.press(['right'])
                                        else:
                                                pyg.press(['left'])
                        else:
                                print(((center[1]-prevcenter[1])/(time.time()-init)))
                                if 175<abs((center[1]-prevcenter[1])/(time.time()-init))<300:
                                        
                                        if center[0]-prevcenter[0] > 0 :
                                                pyg.press(['down'])
                                        else:
                                                pyg.press(['up'])
        init=time.time()
        prevcenter=center
	#print(final)
	#ser.write(final)

	#flag=False
        if cv2.waitKey(1) & ord("q")==0xFF:
                break
ser.close()
