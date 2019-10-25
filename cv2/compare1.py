#coding:utf-8
import face_recognition as fr
import numpy as np
import datetime
import time
import mp3play
import cv2
import MySQLdb
import threading
import pymssql
import sys
from pynput.keyboard import Controller,Key,Listener

#sqlserver
SQL_SERVER_KAOQIN={
'host':'172.16.50.200',
'db':'zkeco',
'user':'sa',
'pwd':'lianluo@12'
}
ms_conn = pymssql.connect(host=SQL_SERVER_KAOQIN['host'],user=SQL_SERVER_KAOQIN['user'],password=SQL_SERVER_KAOQIN['pwd'],database=SQL_SERVER_KAOQIN['db'],timeout=5,login_timeout=2,charset="utf8")
ms_cur = ms_conn.cursor()

#mysql
db = MySQLdb.connect("localhost", "root", "picanoc1119", "face_recognition", charset='utf8' )
cursor = db.cursor()
camera=cv2.VideoCapture(0)
response_ding=mp3play.load("thanks.mp3")
warning_ding=mp3play.load("warning.mp3")
know_face_encodings=[]
know_names=[]
know_pins=[]
inputkey=''
#frame=np.ndarray((480, 640, 3))

# 监听按压
def on_press(key):
    try:
        global inputkey
        inputkey=key.char
    except AttributeError:
        if key.name=="f4":
            inputkey=key.name
# 监听释放
def on_release(key):
    #print("已经释放:",format(key))
 
    if key==Key.esc:
        # 停止监听
        return False

# 开始监听
def start_listen():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

def load_code():
    select_sql="select name,code,pin from userinfo"
    cursor.execute(select_sql)
    result = cursor.fetchall()
    #know_names.append("weijx")
    for name,code,pin in result:
        know_face_encodings.append(np.frombuffer(code))
        know_names.append(name)
        know_pins.append(pin)




def get_codes():
    global frame
    ret,frame=camera.read()
    image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    loc=fr.face_locations(image)
    codes=fr.face_encodings(image,loc)
    return codes

t=threading.Thread(target=start_listen)

def main():
    global inputkey
    print("信息录入系统。\nTips:录入人员信息请按f4键.\n")
    load_code()
    t.start()
    while camera.isOpened():
        time.sleep(2)
        codes=get_codes()
        if inputkey=="f4":
            while True:
                print("请输入信息:")
                name=input("name:")
                know_names.append(name)
                pin=input("pin:")
                know_pins.append(pin)
                for code in codes:
                    know_face_encodings.append(code)
                    if name:
                        coding=code.tobytes()
                        sql = """insert into userinfo(name,code,pin) values(%s,%s,%s)"""
                        print(sql)
                        cursor.execute(sql,(name,coding,pin))
                        db.commit()
                        print("面部信息录入完成。")
                        inputkey=""
                        break

                break
            #ac.restart()
        else:
            for code in codes:
                res=fr.compare_faces(know_face_encodings,code,tolerance=0.40)
                if True in res:
                    index=res.index(True)
                    name=know_names[index]
                    pin=know_pins[index]
                    print("Hello, %s" %name)
                    today=datetime.datetime.now().strftime("%Y-%m-%d")
                    xbtime=datetime.datetime.strptime(today+" 18:00:00","%Y-%m-%d %H:%M:%S")
                    sbtime=datetime.datetime.strptime(today+" 09:30:00","%Y-%m-%d %H:%M:%S")
                    if datetime.datetime.now()>xbtime or datetime.datetime.now()<sbtime:
                        cktime=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000")
                        sql="""insert into checkinout (pin, checktime, checktype, verifycode, WorkCode, Reserved, sn_name) values (%s,%s,%s,%s,%s,%s,%s);"""
                        ms_cur.execute(sql,(pin, cktime, '255', '15', '0', '0', '4104164400102'))
                        ms_conn.commit()
                        response_ding.play()
                    else:
                        print("Sorry,非正常打卡时间")
                    time.sleep(2)
                else:
                    warning_ding.play()
                    #cv2.imshow('monitor', frame)
                    cv2.imwrite('targetPath/%s.jpg'%int(time.time()), frame)
                    # if cv2.waitKey(1) & 0xFF == ord('q'):
                    #     break
                    print("非法人员")
        

        
    db.close()
    camera.release()
    cv2.destroyAllWindows()


main()