import cv2
import numpy as np 

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)


while True:
  _ , frame = cap.read()
  hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  height , width , _ = frame.shape
  cx=int(width/2)
  cy=int(height/2)
  pixel_center=hsv_frame[cy,cx]
  print(pixel_center)
  hue_value=pixel_center[0]
  if hue_value<5 :
    color1="RED"
  elif hue_value<22:
     color1="ORANGE"       
  elif hue_value<33 :
      color1="YELLOW"
  elif hue_value<78 :
      color1="GREEN"  
  elif hue_value<78 :
      color1="GREEN"   
  elif hue_value<131 :
      color1="BLUE"      
  elif hue_value<170 :
      color1="VIOLET"     
  cv2.circle(frame,(cx,cy),5,(255,0,0),3)
  cv2.putText(frame,color1,(10,50),0,1,(255,0,0),2)

  cv2.imshow("frame",frame)
  key=cv2.waitKey(1)
  if key==27 :
    break
  
cap.release()
cv2.destroyAllWindows()



