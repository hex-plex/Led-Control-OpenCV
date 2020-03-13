import cv2
import numpy as np

cam=cv2.VideoCapture(0)
m=cam.read()[1]
r=cv2.selectROI(m)
print(r)
cv2.rectangle(m,tuple([r[1],r[0]]),tuple([r[1]+r[3],r[0]+r[2]]),25)
cv2.imshow('fram',m)
m=cv2.cvtColor(m,cv2.COLOR_BGR2HSV)
cv2.waitKey(1)
m1=m[r[1]:r[1]+r[3],r[0]:r[0]+r[2],:]
cv2.imshow('fra',m1)
cv2.waitKey(1)
bmax=m1[:,:,0].max()
bmin=m1[:,:,0].min()
gmax=m1[:,:,1].max()
gmin=m1[:,:,1].min()
rmax=m1[:,:,2].max()
rmin=m1[:,:,2].min()

lowerskin=np.array([bmin,gmin,rmin])
upperskin=np.array([bmax,gmax,rmax])
print(lowerskin)
print(upperskin)
a=cv2.inRange(m,lowerskin,upperskin)
cv2.imshow("frame",a)

cv2.waitKey(0)
