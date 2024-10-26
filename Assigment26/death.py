import cv2

img = cv2.imread("6.jpg")

for i in range(0,150):
   for j in range(70,120):
          if (j-i >= 0) :
             img[i,j-i] = 0
          
    

cv2.imshow("death symbol", img)
cv2.waitKey()
cv2.imwrite("death_symbol.jpg",img)