# -*- coding: utf-8 -*-
import cv2
from ctypes import *
import datetime
from matplotlib import pyplot

user32=windll.LoadLibrary('user32.dll')

image1=cv2.imread("face.jpg")
def classify_gray_hist(image1,image2):
    hist1 = cv2.calcHist([image1],[0],None,[256],[0.0,255.0])
    hist2 = cv2.calcHist([image2],[0],None,[256],[0.0,255.0])
    #比较直方图
    pyplot.plot(range(256),hist1,'r')
    pyplot.plot(range(256),hist2,'g')
    #pyplot.show()
    #计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1-(abs(hist1[i]-hist2[i])/max(hist1[i],hist2[i])))
        else:
            degree = degree + 1
    degree = degree/len(hist1)
    return degree


def generate():
    stime=datetime.datetime.now()
    face_cascade = cv2.CascadeClassifier(
            r'data\haarcascade_frontalface_alt2.xml')
    camera = cv2.VideoCapture(0)
    count = 0
    time_c=0
    nomatch=0

    while camera.isOpened():
        etime=datetime.datetime.now()
        ret, frame = camera.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        time_c=time_c+len(faces)
        s=etime-stime
        #print s.seconds,time_c,nomatch
        if len(faces)>0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                f = cv2.resize(gray[y: y+h, x:x+w], (256, 256))
                degree=classify_gray_hist(image1,f)
                if degree<=0.4:
                    cv2.putText(frame,"UNAUTHORIZED",(x, y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
                    cv2.imwrite(r'invalidPath/%s.jpg' % str(count), frame)
                    nomatch+=1
                    # cv2.imshow("camera", frame)
                else:
                    # cv2.imshow("camera", frame)
                    pass
            if s.seconds>20:
                # print nomatch
                if time_c==0 or nomatch>=10:
                    with open("d:\\tmp\\log.txt" ,'a') as f:
                        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" window lock,20s get target %d,get not allows target %d\n"%(time_c,nomatch))
                    f.close()
                    user32.LockWorkStation()

                stime = datetime.datetime.now()
                time_c=0   
                nomatch=0
                count += 1
        

        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate()