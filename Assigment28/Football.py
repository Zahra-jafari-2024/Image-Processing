import cv2
import numpy as np

# ایجاد یک تصویر سیاه با ابعاد 133x98
img = np.zeros((450,730, 3), np.uint8)

# تبدیل تصویر به فضای رنگی HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
x=0

# حلقه برای تغییر رنگ بر اساس i
for i in range(7):
    # بررسی اینکه آیا i زوج است یا فرد
    if i % 2 == 0:  # اگر i زوج باشد
        # تغییر رنگ به رنگ آبی در فضای HSV
       img_hsv[:,x:x+105] = [60, 255, 255]  # سبز پررنگ
       x=x+105
        
    else:  # اگر i فرد باشد
        # تغییر رنگ به رنگ قرمز در فضای HSV
       img_hsv[:,x:x+105] = [60, 100, 150]  # سبز کم‌رنگ 
      
       x=x+105

    # تبدیل تصویر از فضای HSV به BGR برای نمایش آن



img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
cv2.rectangle(img_bgr,(10,10), (710,430), (255,255,255), 8)
M1=215
cv2.rectangle(img_bgr,(10,M1-50), (100,M1+50), (255,255,255), 8)
cv2.rectangle(img_bgr,(10,M1-100), (150,M1+100), (255,255,255), 8)

cv2.rectangle(img_bgr,(710,M1-50), (610,M1+50), (255,255,255), 8)
cv2.rectangle(img_bgr,(710,M1-100), (560,M1+100), (255,255,255), 8)

cv2.line(img_bgr,(355 ,0) , (355,430), (255,255,255), 8)

cv2.circle(img_bgr,(355 ,215) , 10, (255,255,255), 8)
cv2.circle(img_bgr,(355 ,215) , 100, (255,255,255), 8)

cv2.imwrite("output/football.jpg" ,img_bgr)
    # نمایش تصویر در هر مرحله
cv2.imshow(f"Iteration ", img_bgr)
    # وقفه برای اینکه هر تغییر رنگ در یک پنجره جداگانه نمایش داده شود
cv2.waitKey(5000) 
 # نمایش به مدت 500 میلی‌ثانیه
cv2.destroyAllWindows()
