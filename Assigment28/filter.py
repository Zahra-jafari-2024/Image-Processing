import cv2
import numpy as np

# Load video and sticker
vi = cv2.VideoCapture("input/video1.mp4")
img_sticker = cv2.imread("input/s.png", cv2.IMREAD_UNCHANGED)  # Load sticker with alpha channel
emoji_eye = cv2.imread('input/eye.png')
emoji_mouth = cv2.imread('input/lip.jpg')
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
lip_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
body_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml")
fps = vi.get(cv2.CAP_PROP_FPS)  # استخراج نرخ فریم
delay = int(1000 / fps)  # محاسبه تأخیر بر حسب میلی‌ثانیه

flag = 0

while True:
    ret, frame = vi.read()
    if not ret:
        print("End of video or error reading frame.")
        break

    key = cv2.waitKey(40) & 0xFF  # Read key pressed

    if key == ord('1'):
        flag = 1
    elif key == ord('2'):
        flag = 2
    elif key == ord('3'):
        flag = 3    
    elif key == ord('4'):
        flag = 4        
    elif key == ord('q'):
        break

    if flag == 1:
        # Detect faces
        faces = face_detector.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            # Resize sticker to fit face
            sticker_resized = cv2.resize(img_sticker, (w, h))
            sticker_rgb = sticker_resized[:, :, :3]
            sticker_alpha = sticker_resized[:, :, 3] / 255.0  # Normalize alpha to range [0, 1]

            # Get region of interest (ROI) in the frame
            roi = frame[y:y+h, x:x+w]

            # Blend sticker with the frame
            for c in range(3):  # Loop over RGB channels
                roi[:, :, c] = roi[:, :, c] * (1 - sticker_alpha) + sticker_rgb[:, :, c] * sticker_alpha

            # Place modified ROI back into the frame
            frame[y:y+h, x:x+w] = roi

    elif flag == 2:
        # Detect eyes
        eyes = eye_detector.detectMultiScale(frame, 1.5, 5)
        for (x, y, w, h) in eyes:
            if w > 0 and h > 0:  # Ensure valid dimensions
                sticker_eye_resized = cv2.resize(emoji_eye, (w, h))
                frame[y:y+h, x:x+w] = sticker_eye_resized
        lips = eye_detector.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in lips:
            if w > 0 and h > 0:  # Ensure valid dimensions
                sticker_lip_resized = cv2.resize(emoji_mouth, (w, h))
                frame[y:y+h, x:x+w] = sticker_lip_resized 

    elif flag == 3:
        faces = face_detector.detectMultiScale(frame , 1.3, minNeighbors=5)
        for face in faces:
            x, y, w, h = face
            blur = frame[y:y+h,x:x+w]
            pixlate = cv2.resize(blur, (20,20), interpolation=cv2.INTER_LINEAR)
            output = cv2.resize(pixlate, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h,x:x+w] = output   

    elif flag == 4:
        bodys = face_detector.detectMultiScale(frame , 1.3)
        for body in bodys:
            x, y, w, h = body
            copy = frame[y:y+h,x:x+w].copy()
            if y + h + h <= frame.shape[0] and x + w + w <= frame.shape[1]:
              frame[y:y+h, x+w:x+w+w] = copy    
            else:
              print("بخش انتخاب شده از مرز تصویر خارج است.")                   
    cv2.imshow("result", frame)
    
vi.release()
cv2.destroyAllWindows()
    
    

