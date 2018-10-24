import json
import requests
import rec
import baidu_voice
import os

# 调用百度asr，录入文字
rec.rec()
input_text = baidu_voice.get_asr('rec_temp.wav')

####################################
# 调用图灵机器人的接口，获得返回的值
####################################
query = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": input_text
                },
                "inputImage": {
                    "url": "imageUrl"
                },
                "selfInfo": {
                    "location": {
                        "city": "",
                        "province": "",
                        "street": ""
                    }
                }
                                                                                        },
                                                                                        "userInfo": {
                                                                                            "apiKey": "5456995947d44f999a3d89819c7da2df",
                                                                                            "userId": "338867"
                                                                                        }
                                                                                                                                                                }

url = 'http://openapi.tuling123.com/openapi/api/v2'

r = requests.post(url, data=json.dumps(query))

output = r.json()
output_text = output.get('results')[0].get('values').get('text')

#########################
# 图灵机器人的请求结束
#########################

# 调用百度TTS，获得语音合成

output_file = baidu_voice.get_tts(output_text)

os.system('mplayer ' + output_file)


