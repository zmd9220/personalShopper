import webview
# import RPi.GPIO as GPIO
import time
import cv2
import pyzbar.pyzbar as pyzbar

import os.path 

import os
import sys
import requests
from pprint import pprint
import json

import pynput

# # Orange : GPIO Pin 12 : 18(Trig)
# TRIG = 18
# # Red : GPIO Pin 18 : 24(Echo)
# ECHO = 24
#
# GPIO.setmode(GPIO.BCM)			# raspbarry 핀 세팅
#
# GPIO.setup(TRIG, GPIO.OUT)			# 18번 핀 out으로 설정
# GPIO.setup(ECHO, GPIO.IN)			# 24번 핀 in 으로 설정


def on_press(key):
    return

def on_release(key):
    if key == pynput.keyboard.Key.shift:
        webview.windows[0].load_url('http://localhost:8080/AdClient')

def on_release_start(key):
    if key == pynput.keyboard.Key.space:
        photo_shot()
        clova_face_recognition()

# 캡쳐
def photo_shot():
    print('photo_shot')
    cap = cv2.VideoCapture(1)	# OpenCV 사진 캡쳐
    ret, frame = cap.read()
    cv2.imwrite('test.jpg', frame)	# 사진의 데이터 test.jpg 저장
    cap.release()

# 얼굴 인식 ( 클로바 )
def clova_face_recognition():
    print('clova')
    client_id = "h_Dm9g2KyYo6TrZtbkMQ"
    client_secret = "d9yEBBJ1rU"
    url = "https://openapi.naver.com/v1/vision/face"  # 얼굴감지

    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    files = {'image': open('test.jpg', 'rb')}
    response = requests.post(url, files=files, headers=headers)
    rescode = response.status_code
    json_data = response.json()

    if json_data['faces']:
        print(json_data)
        gender, gen_confidence = json_data['faces'][0]['gender']['value'], json_data['faces'][0]['gender']['confidence'] # 성별
        age, age_confidence = json_data['faces'][0]['age']['value'], json_data['faces'][0]['age']['confidence']  # 나이
    
        print(gender, gen_confidence)
        print(age[0:2], age_confidence)
        if gender == "female":
            gender = "F"
        else:
            gender = "M"

        webview.windows[0].load_url('http://localhost:8080/{}/{}'.format(age[:2], gender))

    else :
        webview.windows[0].load_url('http://localhost:8080/{}/{}'.format(20, "M"))
    
    #print(webview.windows[0].get_current_url())
    
    if rescode == 200:
        return response.text
    else:
        print("Error Code:" + rescode)
        return "데이터가 없습니다."


# 바코드 스캔
def barcode_scan():
    # OpenCV 사진 캡쳐
    cap = cv2.VideoCapture(1)

    i = 0
    while (cap.isOpened()):
        time.sleep(0.0001)
        # 사진의 데이터 읽기
        ret, img = cap.read()
        
        # 비디오를 제대로 읽었었는지 여부 (사진이 제대로 찍혔는지)
        if not ret:
            continue
        
        # 가져온 화면 데이터를 회색으로 칠하기 - 바코드 인식을 하기 쉽도록
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         # 회색 화면을 토대로 바코드를 찾아 해석
        decoded = pyzbar.decode(gray)
        
        barcode_data = ''
        # 바코드 사각형을 위한 좌표
        for d in decoded:
            x, y, w, h = d.rect

            barcode_data = d.data.decode("utf-8")
            barcode_type = d.type

            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

#            text = '%s (%s)' % (barcode_data, barcode_type)
            # cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
        
        # 인식한 바코드의 숫자가 13자리 일 경우 종료
        if len(barcode_data)==13:
            break;
        # cv2.imshow('img', img)
        

    cap.release()
    cv2.destroyAllWindows()
    
    # 입력 받은 바코드 데이터를 파라미터 값으로 전달
    webview.windows[0].load_url('http://localhost:8080/ProductDetail/{}'.format(barcode_data[9:12]))
    print(barcode_data[9:12])
    #print(webview.windows[0].get_current_url())

# webview 켜진 후 이벤트
def on_loaded():
    # unsubscribe event listener
    webview.windows[0].loaded -= on_loaded
    listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release_start)
    listener.start()
    
    is_ad = False		# 사람 인식 후 광고로 돌아가기 위한 플래그
    cnt = 0		# 사람을 인식한 시간(s)
    try:
        flag = False
        arr = []
        while True:
            # GPIO.output(TRIG, False)
            # time.sleep(0.5)
            #
            # GPIO.output(TRIG, True)
            # time.sleep(0.00001)
            # GPIO.output(TRIG, False)
            #
            # # 18번이 OFF가 되는 시점을 시작시간으로 설정
            # while GPIO.input(ECHO) == 0:
            #     start = time.time()
            #
            # # 18번이 ON이 되는 시점을 반사파 수신시간으로 설정
            # while GPIO.input(ECHO) == 1:
            #     stop = time.time()
            #
            # # 초음파가 되돌아오는 시간차로 거리를 계산한다
            # time_interval = stop - start
            # distance = time_interval * 17000
            # distance = round(distance, 2)

            # url check
            # print(webview.windows[0].get_current_url())
            print('count {}'.format(cnt))
            # 예제 Textfile
            file = './status/barcode.txt'  

            if os.path.isfile(file):
                #print("Yes. it is a file")
                # 바코드 스캔
                barcode_scan()
                # 바코드 스캔 후 파일 제거
                os.remove(file);

            # print("Distance => ", distance, "cm")
            # 50cm 안에 사람이 있을 경우 cnt++
            # if distance <= 50:
            #     cnt += 1
            #     print("거리 => ", distance, "범위 이내 Count : ", cnt)
            # # 사람이 인식되지 않을 경우 cnt 초기화
            # else:
            #     #print(is_ad)
            #     print("거리 => ", distance, "범위 초과")
            #     cnt = 0
            #
            #     #if os.path.isfile(file):
            #     #    os.remove(file);
            #
            #     # 사람이 있다가 떠나면 다시 광고 페이지 호출
            #     if is_ad:
            #         is_ad = False
            #         #print(is_ad)
            #         # 광고 페이지(구글)
            #         # webview.windows[0].load_url('http://localhost:8080/Ad')
            #
            #         webview.windows[0].load_url('http://localhost:8080/AdClient')

            print(webview.windows[0].get_current_url())
            #if webview.windows[0].get_current_url() == 'http://localhost:8080/AdClient':
                #photo_shot()
                #clova_face_recognition()

            # 사람이 키오스크 앞에 3초 서 있는 상황
#             if cnt == 3:
#
#                 is_ad = True
#                 # 메인 페이지 호출 (네이버)
# #                webview.windows[0].load_url('http://localhost:8080')
# #                 webview.windows[0].load_url('https://naver.com')
#                 # 사진 찍는 코드
#                 photo_shot()
#                 # 측정하는 코드
#                 arr = clova_face_recognition()
#
#                 pprint(arr)
#             else:
#                 # 여기는 초기화 하는 코드
#                 arr = []
#                 flag = False
            cnt +=1
            time.sleep(1)

    except KeyboardInterrupt:		# ctrl + c (이걸로 안닫고 stop누르면 다음 실행 시 pin입출력 초기화가 안되서 warning)
        print("Interrupt로 인한 프로그램 종료")
        GPIO.cleanup()			# pin 초기화
        



if __name__ == '__main__':
    # Create a standard webview window
    # 켜지는 중 (없어도 상관x) shown 이벤트에서 호출 됨
    window = webview.create_window('Test browser', 'http://localhost:8080/AdClient'
                                   , fullscreen=True
                                   )

    window.loaded += on_loaded		# 열린 후 이벤트
    webview.start()				# 웹 창 켜기
