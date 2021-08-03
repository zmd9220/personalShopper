import webview
import RPi.GPIO as GPIO
import time
import cv2

import os
import sys
import requests
from pprint import pprint

# 캡쳐
def photo_shot():
    cap = cv2.VideoCapture(0)	# OpenCV 사진 캡쳐
    ret, frame = cap.read()		
    cv2.imwrite('test.jpg', frame)	# 사진의 데이터 test.jpg 저장
    cap.release()

def clova_face_recognition():	
    client_id = "h_Dm9g2KyYo6TrZtbkMQ"
    client_secret = "d9yEBBJ1rU"
    url = "https://openapi.naver.com/v1/vision/face"  # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" // 유명인 얼굴인식

    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    files = {'image': open('/home/pi/Desktop/test.jpg', 'rb')}
    response = requests.post(url, files=files, headers=headers)
    rescode = response.status_code

    #print(rescode)

    if rescode == 200:
        return response.text
    else:
        print("Error Code:" + rescode)
        return "데이터가 없습니다."


def goto_front(data):
    # 프론트에 데이터를 받아서 넘기기
    pass
    # return reqeusts.status_code

def on_closed():			# webview 닫힌 후 이벤트
    print('pywebview window is closed')

def on_closing():			# webview 닫히는 중 이벤트
    print('pywebview window is closing')

def on_shown():			# webview 켜지는 중 이벤트
    print('pywebview window shown')

def on_loaded():			# webview 켜진 후 이벤트
    # unsubscribe event listener
    webview.windows[0].loaded -= on_loaded		
    webview.windows[0].load_url('https://google.com')	# 웹뷰가 켜지면 광고(구글) 이 뜸
    
    is_ad = False		# 사람 인식 후 광고로 돌아가기 위한 플래그
    cnt = 0		# 사람을 인식한 시간(s)
    try:
        flag = False
        arr = []
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
            if distance <= 50:		# 50cm 안에 사람이 있을 경우 cnt++
                cnt += 1
                print("거리 => ", distance, "범위 이내 Count : ", cnt)
            else:			# 사람이 인식되지 않을 경우 cnt 초기화
                print(is_ad)
                print("거리 => ", distance, "범위 초과")
                cnt = 0
                if is_ad==True :		# 사람이 있다가 떠나면 다시 광고 페이지 호출
                    is_ad=False
                    print(is_ad)
                    webview.windows[0].load_url('https://www.google.com/%27)		# 광고 페이지(구글)


            if cnt == 3:		# 사람이 키오스크 앞에 3초 서 있는 상황
                is_ad = True
                webview.windows[0].load_url('https://www.naver.com/%27)	# 메인 페이지 호출 (네이버)
                # 사진 찍는 코드
                photo_shot()
                # 측정하는 코드
                arr = clova_face_recognition()
                pprint(arr)


            else:
                # 여기는 초기화 하는 코드
                arr = []
                flag = False

            time.sleep(1)

    except KeyboardInterrupt:		# ctrl + c (이걸로 안닫고 stop누르면 다음 실행 시 pin입출력 초기화가 안되서 warning)
        print("Interrupt로 인한 프로그램 종료")
        GPIO.cleanup()			# pin 초기화
# Orange : GPIO Pin 12 : 18(Trig)
TRIG = 18				
# Red : GPIO Pin 18 : 24(Echo)
ECHO = 24

GPIO.setmode(GPIO.BCM)			# raspbarry 핀 세팅

GPIO.setup(TRIG, GPIO.OUT)			# 18번 핀 out으로 설정
GPIO.setup(ECHO, GPIO.IN)			# 24번 핀 in 으로 설정



if name == 'main':
    # Create a standard webview window
    # 켜지는 중 (없어도 상관x) shown이벤트에서 호출 됨
    window = webview.create_window('Simple browser', 'https://pywebview.flowrl.com/hello%27)	
    window.closed += on_closed		# 닫힌 후 이벤트
    window.closing += on_closing		# 닫히는 중 이벤트
    window.shown += on_shown		# 열리는 중 이벤트
    window.loaded += on_loaded		# 열린 후 이벤트
    webview.start()				# 웹 창 켜기