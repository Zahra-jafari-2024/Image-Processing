import numpy as np
import cv2

img = np.zeros((255, 255), np.uint8)
for i in range(255):
    for j in range(255):
        img[i,j]=255-i ;
cv2.imshow("Generate", img)
cv2.waitKey()
cv2.imwrite("result\Generate.jpg",img)