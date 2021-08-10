import webview
import RPi.GPIO as GPIO
import time
import cv2

import os.path 

import requests
from pprint import pprint

# Orange : GPIO Pin 12 : 18(Trig) 송신부
TRIG = 18
# Red : GPIO Pin 18 : 24(Echo) 수신부
ECHO = 24

# raspbarry 핀 세팅
GPIO.setmode(GPIO.BCM)

# 18번 핀 out으로 설정 - 송신
GPIO.setup(TRIG, GPIO.OUT)
# 24번 핀 in 으로 설정 = 수신
GPIO.setup(ECHO, GPIO.IN)


def photo_shot():
    # OpenCV를 통해 카메라를 작동시켜서 캡쳐
    cap = cv2.VideoCapture(0)
    # 캡쳐 화면의 데이터 읽기
    ret, frame = cap.read()
    # 사진의 데이터 test.jpg 저장
    cv2.imwrite('test.jpg', frame)
    # 캡쳐 화면 데이터 해제
    cap.release()


def clova_face_recognition():
    # Naver Developers에서 발급받은 개인 키 - 지역 변수로 암호화 필요..
    client_id = "h_Dm9g2KyYo6TrZtbkMQ"
    client_secret = "d9yEBBJ1rU"
    url = "https://openapi.naver.com/v1/vision/face"  # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

    # API 요청을 위한 헤더 양식
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    # 같이 보낼 image 파일 설정
    files = {'image': open('/home/pi/Desktop/test.jpg', 'rb')}
    # API server에 POST요청을 보내고 응답을 받은 결과물이 들어 있는 response 객체
    response = requests.post(url, files=files, headers=headers)
    # 응답 코드를 보기 위한 rescode
    rescode = response.status_code

    if rescode == 200:
        return response.text
    else:
        print("Error Code:" + rescode)
        return "데이터가 없습니다."


# webview 닫힌 후 이벤트
def on_closed():
    print('pywebview window is closed')


# webview 닫히는 중 이벤트
def on_closing():
    print('pywebview window is closing')


# webview가 켜지는 중 이벤트
def on_shown():
    print('pywebview window shown')


# webview가 켜진 후 이벤트
def on_loaded():
    # unsubscribe event listener
    webview.windows[0].loaded -= on_loaded
    
    # 사람 인식 후 광고로 돌아가기 위한 플래그
    is_ad = True
    # 사람을 인식한 시간(s)
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

            # 초음파가 되돌아오는 시간차로 거리를 계산
            time_interval = stop - start
            distance = time_interval * 17000
            distance = round(distance, 2)


            file = 'C:\\Users\\multicampus\\Downloads\\barcode.txt'     # 예제 Textfile

            if os.path.isfile(file):
               print("Yes. it is a file")


            # 50cm 안에 사람이 있을 경우 cnt++
            if distance <= 50:
                cnt += 1
                print("거리 => ", distance, "범위 이내 Count : ", cnt)
            # 사람이 인식되지 않을 경우 cnt 초기화
            else:
                print("거리 => ", distance, "범위 초과")
                cnt = 0
                # 사람이 있다가 떠나면 다시 광고 페이지 호출
                if not is_ad:
                    is_ad = True
                    # 광고 페이지(AdClient)
                    webview.windows[0].load_url('http://localhost:8080/AdClient')

            # 사람이 키오스크 앞에 3초 서 있는 상황
            if cnt == 3:
                # 광고 페이지 이동 막기
                is_ad = False
                # 메인 페이지 호출 (localhost)
                webview.windows[0].load_url('http://localhost:8080/')
                # 사진 찍는 코드
                photo_shot()
                # 얼굴 인식, 측정 하는 코드
                pprint(clova_face_recognition())
            
            time.sleep(1)
    # ctrl + c (이걸로 안닫고 stop을 누르면 다음 실행 시 pin 입출력이 초기화가 안되서 warning 메세지가 뜸)
    except KeyboardInterrupt:
        print("Interrupt로 인한 프로그램 종료")
        # pin 초기화
        GPIO.cleanup()



if __name__ == '__main__':
    # Create a standard webview window
    # 켜지는 중 (없어도 상관x) shown 이벤트에서 호출 됨
    window = webview.create_window('Test browser', 'http://localhost:8080/AdClient')
    # 닫힌 후 이벤트
    window.closed += on_closed
    # 닫히는 중 이벤트
    window.closing += on_closing
    # 열리는 중 이벤트
    window.shown += on_shown
    # 열린 후 이벤트
    window.loaded += on_loaded
    # 웹 창 켜기
    webview.start()

