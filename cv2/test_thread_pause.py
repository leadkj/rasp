#coding:utf-8
import threading
import sys
import time
class addCode(threading.Thread):
    i=2
    input_str=""
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.singal=threading.Event()
        self.singal.set()
        
    def run(self):
        while 1:
            print("child")
            input_kb = str(sys.stdin.readline()).strip("\n")
            print(input_kb,"stdin")
            if input_kb=='s':   #stop
                self.i=1
                print("人员信息开始录入,按enter开始.",end="")
            elif input_kb=="q":    #continue
                self.i=0
                print("操作完成,请按enter键")
                self.input_str=input_kb
                break
            else:
                self.input_str=input_kb
    def pause(self):
        self.singal.clear()
    def restart(self):
        self.singal.set()


ac=addCode()
ac.start()

time.sleep(3)
ac.pause()