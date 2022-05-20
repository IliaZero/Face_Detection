import cv2

file_path = "elon-musk.jpg"

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
pic = cv2.resize(cv2.imread(file_path), (756, 512))
gray_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_pic, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 255, 255), 2)

cv2.imshow("test", pic)
cv2.waitKey(0)
