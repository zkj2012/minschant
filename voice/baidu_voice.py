# 把百度的asr和tts接口做了两个函数
# 这里的token是提前取好写死的，理论上会过期，需要用两个key重取
# get_asr的输入是文件名全名,输出是识别出来的文字
# get_tts的输入是需要识别的中文,输出是音频文件名全名

# coding=utf-8

import sys
import json
import base64

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus


# API_KEY = 'yGPhPGOigduM5BsQc0QE7agR'
# SECRET_KEY = 'B3QoQDLRDG8BuLW9TTNRi9Hymgt5BytF'


def get_asr(file_name):

	token = '24.c5ba6738c89c35e7c83ac21a88c1979e.2592000.1542298163.282335-14317689'

	# 需要识别的文件
	AUDIO_FILE = './' + file_name#只支持 pcm/wav/amr
	# 文件格式
	FORMAT = AUDIO_FILE[-3:];  # 文件后缀 pcm/wav/amr
	# 根据文档填写PID，选择语言及识别模型
	DEV_PID = 1536;  # 1537 表示识别普通话，使用输入法模型。1536表示识别普通话，使用搜索模型

	CUID = '123456PYTHON';
	# 采样率
	RATE = 16000;  # 固定值

	ASR_URL = 'http://vop.baidu.com/server_api'


	speech_data = []
	with open(AUDIO_FILE, 'rb') as speech_file:
		speech_data = speech_file.read()
	length = len(speech_data)
	speech = base64.b64encode(speech_data)
	speech = str(speech, 'utf-8')
	params = {'dev_pid': DEV_PID,
			  'format': FORMAT,
			  'rate': RATE,
			  'token': token,
			  'cuid': CUID,
			  'channel': 1,
			  'speech': speech,
			  'len': length
			  }
	post_data = json.dumps(params, sort_keys=False)


	# print post_data
	req = Request(ASR_URL, post_data.encode('utf-8'))
	req.add_header('Content-Type', 'application/json')
	f = urlopen(req)
	result_str = f.read()
	result_str = str(result_str, 'utf-8')
	result_json = json.loads(result_str)
	result_words = result_json['result'][0]
	return(result_words)


def get_tts(TEXT):

	token = '24.91730876b8a89f1498ce4f4c9e68bde1.2592000.1542345536.282335-14317689'



	# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
	PER = 4
	# 语速，取值0-15，默认为5中语速
	SPD = 5
	# 音调，取值0-15，默认为5中语调
	PIT = 5
	# 音量，取值0-9，默认为5中音量
	VOL = 5
	# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
	AUE = 3

	FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
	FORMAT = FORMATS[AUE]

	CUID = "123456PYTHON"

	TTS_URL = 'http://tsn.baidu.com/text2audio'

	TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
	SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选


	tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode

	params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

	data = urlencode(params)
	req = Request(TTS_URL, data.encode('utf-8'))
	f = urlopen(req)
	result_str = f.read()

	save_file =  'result.' + FORMAT
	with open(save_file, 'wb') as of:
		of.write(result_str)

	print("result saved as :" + save_file)

	return(save_file)
