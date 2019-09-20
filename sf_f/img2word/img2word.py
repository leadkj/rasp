
#coding:utf-8
import sys
from aip import AipOcr
APP_ID='17137507'
API_KEY = 'h4tkLq9hM4r1XSM8NpoBq2Kw'
SECRET_KEY = 'm1WEhso1O9rkwVv2UEpDx5N27iM1EV6W'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filePath=sys.argv[1]
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(filePath)
# client.basicGeneral(image);
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"

# """ 带参数调用(高精度)通用文字识别, 图片参数为本地图片 """
# res=client.basicAccurate(image, options) #basicGeneral通过识别
# for i in res['words_result']:
# 	try:
# 		print i['words']
# 	except Exception as e:
# 		pass
""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["baike_num"] = 5
""" 带参数调用车辆识别 """
client.carDetect(image, options)