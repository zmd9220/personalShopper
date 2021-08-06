import RPi.GPIO as GPIO
import time

# Orange : GPIO Pin 12 : 18(Trig)
TRIG = 18
# Red : GPIO Pin 18 : 24(Echo)
ECHO = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

cnt = 0
try:
    while True:
        GPIO.output(TRIG, False)
        time.sleep(0.5)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # 18번이 OFF가 되는 시점을 시작시간으로 설정
        while GPIO.input(ECHO) == 0:
            start = time.time()

        # 18번이 ON이 되는 시점을 반사파 수신시간으로 설정
        while GPIO.input(ECHO) == 1:
            stop = time.time()

        # 초음파가 되돌아오는 시간차로 거리를 계산한다
        time_interval = stop - start
        distance = time_interval * 17000
        distance = round(distance, 2)

        # print("Distance => ", distance, "cm")
        if distance <= 50:
            cnt += 1
        else:
            cnt = 0

        if cnt > 3:
            print("Distance => ", distance, "on!!!!")
        else :
            print("Distance => ", distance, "off")
            
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()