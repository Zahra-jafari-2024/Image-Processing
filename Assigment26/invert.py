import cv2
imgs = cv2.imread("1.jpg")


height = imgs.shape[0]
width= imgs.shape[1]
for i in range(height):
    for j in range(width):
        imgs[i, j] = 255 - imgs[i, j]

imgs1 = cv2.imread("2.jpg")


height = imgs1.shape[0]
width= imgs1.shape[1]
for i in range(height):
    for j in range(width):
        imgs1[i, j] = 255 - imgs1[i, j]

#imgs =cv2.resize(imgs,(400, 400))
cv2.imshow("output", imgs1)
cv2.waitKey()
cv2.imwrite("result\invert2.jpg",imgs1)

cv2.imshow("output", imgs)
cv2.imwrite("result\invert1.jpg",imgs)
cv2.waitKey()
