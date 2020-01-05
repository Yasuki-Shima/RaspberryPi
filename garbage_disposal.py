#!/usr/bin/env python3
#encoding=utf-8
## check for garbage disposal
## スクリプト名：garbage_disposal.py
## 機能概要　　：ゴミ出しを判断しLEDでお知らせする
##
## Presented by RASPI MAG
## Programmed by pochi_ken
# ライブラリー定義
import RPi.GPIO as GPIO
import time
import sys
import os
import os.path
import datetime

conffile = 'garbage_disposal.conf'
cday = datetime.date.today().strftime("%Y%m%d")


def readconf():
# ゴミ出し判断ファイルの読み込み
    cweek = datetime.date.today().strftime("%a")
    if os.path.isfile(conffile):
        f = open(conffile, 'r')
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                garbage, weeks = line[:-1].split(',')
                for week in weeks.split(':'):
                    if week == cweek:
                        led_on(LED_list[int(garbage) - 1])
        f.close()
    else:
        print("garbage_disposal.confファイルがありません")
        exit()

def led_on(LED):
    GPIO.output(LED, True)

def led_off(LEDs):
    GPIO.output(LEDs, [0, 0, 0])

def event(switch):
    led_off(LED_list)

# setting up GPIO
GPIO.setmode(GPIO.BOARD)          #       use GPIO numbering convention
GPIO.setwarnings(False)
LED_list = [11, 13, 15]           # 1, 2, 3用のLEDGPIO
switch = 19                       # タクトスイッチ
GPIO.setup(LED_list, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(switch, GPIO.FALLING, bouncetime=200)
GPIO.add_event_callback(switch, event)
led_off(LED_list)

# Main
try:
    readconf()
    while True:
        time.sleep(2)
        today = datetime.date.today().strftime("%Y%m%d")
        if today != cday:
            cday = today
            led_off(LED_list)
            readconf()
        else:
            pass
	print(today)

except KeyboardInterrupt:
    GPIO.cleanup()
