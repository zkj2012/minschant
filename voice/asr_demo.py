import rec
import baidu_voice

TEXT = rec.rec()

TEXT = baidu_voice.get_asr('rec_temp.wav')

print('识别的结果是： ' + TEXT)
