#coding:utf-8
import sys
from aip import AipOcr
APP_ID='17137507'
API_KEY = 'h4tkLq9hM4r1XSM8NpoBq2Kw'
SECRET_KEY = 'm1WEhso1O9rkwVv2UEpDx5N27iM1EV6W'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filePath=sys.argv[1]
""" ��ȡͼƬ """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(filePath)
# client.basicGeneral(image);
""" ����п�ѡ���� """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" ����������(�߾���)ͨ������ʶ��, ͼƬ����Ϊ����ͼƬ """
res=client.basicAccurate(image, options) #basicGeneralͨ��ʶ��
for i in res['words_result']:
	try:
		print i['words']
	except Exception as e:
		pass