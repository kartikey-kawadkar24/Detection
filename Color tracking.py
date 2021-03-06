import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while(1): 
    _,frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    # hsv hue sat value
    
    lower_red = np.array([161, 155, 84]) 
    upper_red = np.array([179, 255, 255]) 
    
    mask = cv2.inRange(hsv, lower_red, upper_red) 
    result = cv2.bitwise_and(frame, frame, mask = mask) 
    
    cv2.imshow('frame', frame) 
    cv2.imshow('mask', mask) 
    cv2.imshow('result', result) 
    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break
cv2.destroyAllWindows() 
cap.release() 
