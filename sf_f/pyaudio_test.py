#coding:utf-8
import signal
import snowboydecoder
import pyaudio
import wave
from playsound import playsound
from aip import AipSpeech
import os
import threading
import sys 
reload(sys)
sys.setdefaultencoding('utf8')
record_file='/tmp/output.wav'  ##录音文件位置
Synt_file="/tmp/ans.mp3"  ##合成语音文件位置

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted





##录音
def RecordFun(record_file):
    CHUNK=1024
    FORMAT=pyaudio.paInt16
    CHNANELS=1
    RATE=16000
    RECORD_SECONDS=5
    WAVE_OUTPUT_FILENAME=record_file
    pa=pyaudio.PyAudio()
    stream=pa.open(format=FORMAT,channels=CHNANELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    frames=[]
    for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
        data=stream.read(CHUNK)
        frames.append(data)
    print "luyin over"
    stream.stop_stream()
    stream.close()
    pa.terminate()
    print "save file"
    wf=wave.open(WAVE_OUTPUT_FILENAME,'wb')
    wf.setnchannels(CHNANELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print "save over"
def RecordFun2(record_file):
    print "start record......."
    os.popen('arecord -D "plughw:1,0" -d 5 -f cd -r 16000 -c 1 > %s' %record_file)
    print  "rcord over...."
##语音识别
def AsrFun(record_file):

    APP_ID = '10716022'
    API_KEY = '6urHctvfU0P3jtSQ8rnbqoAP'
    SECRET_KEY = 'tKZXLDaz807YhY8PaGvt84PLdWOxHDVq'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    def get_file(file):
        with open(file) as f:
            return f.read()  
    asr_res=client.asr(get_file(record_file),'wav',16000,{'dev_pid':1536})
 #   os.remove(record_file)
    if asr_res["err_msg"]=="success.":
        print asr_res["result"][0]
        from Motor import TRun
        from jdq  import Ton,Toff
        from  FanControl import TFon,TFonyt
        if asr_res["result"][0]=="打开窗帘":
            t=threading.Thread(target=TRun,args=(0,4000))
            t.setDaemon(True)
            t.start() 
            #TRun(0,4000)
        elif asr_res["result"][0]=="关闭窗帘":
            t=threading.Thread(target=TRun,args=(1,4000))
            t.setDaemon(True)
            t.start() 
            #TRun(1,4000)
        elif asr_res["result"][0]=="开灯":
            Ton()
        elif asr_res["result"][0]=="关灯":
            Toff()
        elif asr_res["result"][0]=="打开风扇":
            TFon()
        elif asr_res["result"][0]=="关闭风扇":
            TFon()
        elif asr_res["result"][0]=="摇头":
            TFonyt()
        elif asr_res["result"][0]=="暂停":
            TFonyt()
        #result=client.synthesis(asr_res["result"][0],'zh',1,{'vol':5,})
        #PlayRes(result,Synt_file)
    #return asr_res
    return None


#根据识别内容，把回复内容合成语音进行播放回复
#Synt_content=AsrFun(record_file)
def SyntFun(Synt_content):
    if Synt_content.has_key("result"):
        if Synt_content['result'][0]=="你说鸡蛋":
            result=client.synthesis("我说要",'zh',1,{'vol':5,})
            PlayRes(result)
        elif Synt_content['result'][0]=="鸡蛋鸡蛋":
            result=client.synthesis("要要",'zh',1,{'vol':5,})
            PlayRes(result)
        else:
            result=client.synthesis("不要",'zh',1,{'vol':5,})
            PlayRes(result)


##播放结果
def PlayRes(result,Synt_file):
    if not isinstance(result,dict):
        with open(Synt_file,'wb') as f:
            f.write(result)
    #playsound(Synt_file)
    os.popen("play %s" %Synt_file)
    #playsound(Synt_file)
    #os.remove(Synt_file)

def callbacks():
    global detector
    snowboydecoder.play_audio_file()
    detector.terminate()
    RecordFun(record_file)
    res=AsrFun(record_file)
    wake_up()
def wake_up():
    global detector
    model = 'xb.pmdl'

    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    detector.start(detected_callback=callbacks,interrupt_check=interrupt_callback,sleep_time=0.03)

    detector.terminate()
if  __name__=='__main__':
    #RecordFun2(record_file)
    #res=AsrFun(record_file)
    #print res
    wake_up()
