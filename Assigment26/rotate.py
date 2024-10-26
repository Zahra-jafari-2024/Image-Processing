import numpy as np
import cv2

img=cv2.imread('3.jpg')
height, width = img.shape[:2]
image_center = (width/2, height/2)
rotation_matrix = cv2.getRotationMatrix2D(image_center, 180, 1.0)
rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)
cv2.imwrite("result\3.jpg", rotated_image) 
cv2.imshow("result", rotated_image) 
cv2.waitKey()

