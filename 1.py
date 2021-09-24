import cv2
import numpy as np
import time

cap = cv2.VideoCapture("cottonvideo.mp4")


whiteLower = (50,0,90)
whiteUpper = (240,10,240)
kernel = np.ones((5,5), dtype = np.uint8) 


while True:
    
    success, frame = cap.read()
    
    #frame = cv2.resize(frame, dsize=(640,360))
    blur = cv2.GaussianBlur(frame,(5,5),0)
    kernel = np.ones((4,4),np.uint8)
    dilation = cv2.dilate(blur,kernel,iterations = 1)
    
    if success :
        
        
        
        whiteLower = (0,0,130)
        whiteUpper = (15,70,255)
    
 
        hsv = cv2.cvtColor(dilation, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, whiteLower, whiteUpper)
        cv2.imshow("Sonuc", mask)
        

        # Find contours, obtain bounding rect, and draw width
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            
            x,y,w,h = cv2.boundingRect(c)
            
            #print("Width:" , w, "Height:" ,h)
            
            if 20>w or 20>h:
                pass
            else:
                 cv2.rectangle(frame, (x, y), (x + w, y + h), (36,255,12), 4)
            #cv2.putText(frame, str(w), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
           

        cv2.imshow("Orijinal", frame)
       

        time.sleep(0.05)


    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break


cap.release()
cv2.destroyAllWindows()
