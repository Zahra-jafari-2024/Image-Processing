import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    rec,frame=cap.read()
    frame_shv=cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    cv2.imshow("result" , frame)
    keyexit=cv2.waitKey(5) & 0XFF
    if keyexit==27 :
        break
cv2.destroyAllWindows()
cap.release()    