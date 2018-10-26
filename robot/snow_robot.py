#coding=utf-8

import snowboydecoder
import sys
import signal
import rec
import baidu_voice
import json
import requests
import os

def robot():

    # 先关闭监听，已解决麦克风占用问题

    detector.terminate()

    # 播放一个音效，以提示开始录音了

    os.system('mplayer conan.mp3')

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

    return()

def print_text():
    print('你有啥事')
    return()




interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=robot,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.start(detected_callback=robot,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
