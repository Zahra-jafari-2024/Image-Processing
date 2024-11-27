import cv2

img=cv2.imread("input/cat_image.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cat_detector=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalcatface_extended.xml")
cats=cat_detector.detectMultiScale(img_gray ,1.01)
x=0
for cat in cats:
    x=x+1
    print(cat)


print(x)
cv2.waitKey(5000)            
cv2.destroyAllWindows()