import cv2
import numpy as np


image=cv2.imread("batman.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )

rows,cols=image.shape


threshold=140

ret,binary =cv2.threshold(image,threshold,255,cv2.THRESH_BINARY)

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org

org = (350, 450)

# fontScale
fontScale = 2
 
# Red color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 2
 
# Using cv2.putText() method
image = cv2.putText(binary, "BATMAN", org, font, fontScale, 
                 color, thickness, cv2.LINE_AA, False)


cv2.imshow("result",binary)
cv2.imwrite("output/batman_lo.jpg",binary)
cv2.waitKey()
