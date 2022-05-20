import cv2

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
while True:
    success, frame = cam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("cam", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break