# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

#ボードの番号で設定(目で見て数えるやつ)
GPIO.setmode(GPIO.BOARD)

#LED定義
LD1 = 19
LD2 = 21
LD3 = 23
LD4 = 27
#LEDのポート宣言
GPIO.setup(LD1, GPIO.OUT)
GPIO.setup(LD2, GPIO.OUT)
GPIO.setup(LD3, GPIO.OUT)
GPIO.setup(LD4, GPIO.OUT)
#LED消灯
GPIO.output(LD1, GPIO.LOW)
GPIO.output(LD2, GPIO.LOW)
GPIO.output(LD3, GPIO.LOW)
GPIO.output(LD4, GPIO.LOW)

#SW定義
SW1 = 31
SW2 = 33
SW3 = 35
SW4 = 37
#SWのポート宣言
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#スピーカー定義
SP = 40
#スピーカーのポート宣言
GPIO.setup(SP, GPIO.OUT)

#PWMインスタンス生成
BELL = GPIO.PWM(SP, 30)
BELL.start(50) #デューティーサイクル50%固定
BELL.stop()

#平均(しかも切り上げ)律音階周波数
mel_C = 262 #ド
mel_D = 294 #レ
mel_E = 330 #ミ
mel_F = 349 #ファ
mel_G = 392 #ソ
mel_A = 440 #ラ
mel_B = 494 #シ

#LEDステータス用の変数
status_LD1 = False
status_LD2 = False
status_LD3 = False
status_LD4 = False

#成功回数
Hits = 0
#全体ループ用
Loop = 10

def Lit(gpioNo, status)
    GPIO.output(gpioNo, status)

def HitBell()
    Bell.start(0.05)
    Bell.ChangeFrequency(mel_C)
    time.sleep(0.05)
    Bell.ChangeFrequency(mel_D)
    time.sleep(0.05)
    Bell.ChangeFrequency(mel_E)
    time.sleep(0.05)
    Bell.stop(0)

def MissBell()
    Bell.start(50)
    Bell.ChangeFrequency(100)
    time.sleep(0.05)
    Bell.ChangeFrequency(100)
    time.sleep(0.05)
    Bell.stop(0)

def Hit()
    HitBell()
    Hits += 1

if __name__ =- '__main__'
    print("programm start\n")
    try:
        while true:
            for i in range(0, Loop):
                for j in range(1, 500):
                    if (GPIO.input(SW1) and GPIO.input(SW2) and GPIO.input(SW3) and GPIO.input(SW4)):
                        MissBell()
                        MissBell()
                        break
                    elif (GPIO.output and GPIO.input(SW1)):
                        Hit()
                        break
                    else:
                        Lit(LD1, true)
                        time.sleep(0.002)
                    if (j == 499):
                        MissBell()

                Lit(LD1, false)
                sleep(0.001)

    except KeyboardInterrupt:
        print("detect key interrupt\n")

    finally:
        BELL.stop()
        GPIO.cleanup()
        print("program exit\n")