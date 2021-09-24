import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import time

img = cv.imread("frame2")
img = cv.resize(img, (864,546))

blur = cv.GaussianBlur(img,(5,5),0)
kernel = np.ones((4,4),np.uint8)
dilation = cv.dilate(blur,kernel,iterations = 1)

hsv = cv.cvtColor(dilation, cv.COLOR_BGR2HSV)

def nothing(x):
    pass

whiteLower = (0,0,0)
whiteUpper = (0,0,0)

cv.namedWindow('image')
cv.resizeWindow("image", 600,300)
cv.createTrackbar('H1','image',0,179,nothing)
cv.createTrackbar('H2','image',0,179,nothing)
cv.createTrackbar('V1','image',0,255,nothing)
cv.createTrackbar('V2','image',0,255,nothing)
cv.createTrackbar('S1','image',0,255,nothing)
cv.createTrackbar('S2','image',0,255,nothing)


while True:
    

    
    
    H1 = cv.getTrackbarPos('H1','image')
    S1 = cv.getTrackbarPos('S1','image')
    V1 = cv.getTrackbarPos('V1','image')
    
    H2 = cv.getTrackbarPos('H2','image')
    S2 = cv.getTrackbarPos('S2','image')
    V2 = cv.getTrackbarPos('V2','image')
    
    whiteLower = (H1,S1,V1)
    whiteUpper = (H2,S2,V2)
    
    
    mask = cv.inRange(hsv, whiteLower, whiteUpper)
    result = cv.bitwise_and(dilation, dilation,mask)
   
    
    
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    hStack = np.hstack([mask,result])
    cv.imshow("Horizontal Stacking", hStack)
    
    

    if cv.waitKey(1) & 0xFF == ord("q"): break

cv.destroyAllWindows()
    
    
    
    
    
    
    