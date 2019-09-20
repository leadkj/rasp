#coding:utf-8
from aip import AipImageClassify
import sys

APP_ID='17137507'
API_KEY = 'h4tkLq9hM4r1XSM8NpoBq2Kw'
SECRET_KEY = 'm1WEhso1O9rkwVv2UEpDx5N27iM1EV6W'

filePath=sys.argv[1]
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image=get_file_content(filePath)
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["baike_num"] = 5
""" 带参数调用车辆识别 """
res=client.carDetect(image, options)
for i in res['result']:
	if i['baike_info']:
		print i['name']
		print i['baike_info']['description']
	else:
		print i['name']