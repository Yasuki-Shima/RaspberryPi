#!/usr/bin/env python3
#encoding=utf-8
## check for room's humidity
## スクリプト名：room_humidity.py
## 機能概要　　：部屋の乾燥をチェックする
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
import dht11

# setting up GPIO
GPIO.setmode(GPIO.BOARD)          #       use GPIO numbering convention
GPIO.setwarnings(False)

BEEP = 13          # 電子ブザー
DHT = 11           # DHT11
GPIO.setup(BEEP, GPIO.OUT)
instance = dht11.DHT11(pin=DHT)

# Main
try:
    while True:
        result = instance.read()
        if result.is_valid():
            hum = result.humidity
            if hum < 80 and hum >70:
                for i in range(4):
                    GPIO.output(BEEP, (1 - GPIO.input(BEEP)))
                    time.sleep(0.25)
            elif hum > 80:
                for i in range(10):
                    GPIO.output(BEEP, (1 - GPIO.input(BEEP)))
                    time.sleep(0.10)
            else:
                time.sleep(1)
            print("Humidity: %d %%" % hum)
            
except KeyboardInterrupt:
    GPIO.cleanup()
