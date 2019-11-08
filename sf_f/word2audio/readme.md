##更换apt源
sudo vi /etc/apt/sources.list
deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi
sudo vi /etc/apt/sources.list.d/raspi.list
deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ stretch main ui

##安装pyttsx3(文字转语音)
1， 安装espeak
	sudo apt-get install espeak
2,  安装pyttsx3
	sudo pip3 install pyttsx3


##安装面目识别模块face-recogintion
1，安装opencv
2，安装cmake
	sudo pip3 install cmake
2, 安装dlib
3, 安装face-recognition


##安装语音识别模块SpeechRecognition  
(https://blog.csdn.net/Imliao/article/details/98911100,
https://blog.csdn.net/Imliao/article/details/98911100)

1,安装SpeechRecognition
	sudo pip3 install SpeechRecognition
2,安装swig
	sudo apt-get install swig
3,安装libpulse-dev 
	sudo apt-get install libpulse-dev 
4,安装libasound2-dev
	sudo apt-get install libasound2-dev
3,安装pocketsphinx
	sudo pip3 install pocketsphinx

e.g.

import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)


##p