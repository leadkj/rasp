import cv2


face_cascade = cv2.CascadeClassifier('data\haarcascade_frontalface_alt2.xml')

img = cv2.imread('timg.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
print len(faces)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()