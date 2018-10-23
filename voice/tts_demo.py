import baidu_voice
import os

TEXT = input('请输入需要发音的中文:')
baidu_voice.get_tts(TEXT)

os.system('mplayer result.mp3')
