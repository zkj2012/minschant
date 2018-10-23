#!/bin/bash                                                                                                                                                  
# A touch-switch control program.                                                                                                                            
 
# the Raspberry Pi GPIO input pin number, namely the pin connected to the signal output pin of the toch-switch module                                        
GPIO_PORT=8
 
# set the specified GPIO port to INPUT mode                                                                                                                  
gpio mode $GPIO_PORT in
 
while true
do
	 SWITCH_STATUS=`gpio read $GPIO_PORT`
	 if [ $SWITCH_STATUS -eq 1 ]; then
		python3 ~/minschantGit/voice/tts_demo.py  # 这里输入要想运行的程序，之后触摸开关就会运行了
		# echo "Pressed @ `date +\"%F %T\"`"
	fi
	sleep 0.01
done
