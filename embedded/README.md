# 임베디드 README



### 설치 및 기본 세팅

#### 설치 + 키보드 세팅 - ibus

- https://kwonkyo.tistory.com/398 참고하여 진행 (설치)

```bash
# 한글 키보드 설치 코드
pi@raspberrypi :~ $ sudo apt-get install ibus
pi@raspberrypi :~ $ sudo apt-get install ibus-hangul
pi@raspberrypi :~ $ sudo apt-get install fonts-unfonts-core
```

- 설치가 완료되면 "시작 > Preferences > IBus Prefrences" 메뉴를 통해 IBus설정창을 열어줍니다.

![ibus](README.assets/ibus.png)





- 처음에 IBus가 실행되고 있지 않다면 실행하겠냐는 확인창이 뜨고 다음으로 다음과 같이 실행에 문제가 있을 때 취할 수 있는 조치사항을 보여주는 창이 나타납니다. 제 경우 별 문제없었기 때문에 그냥 무시합니다.

![ibus1](README.assets/ibus1.png)



- 설정창에서 Input 탭을 열어보면 영어만 보이는데요 여기에 한글 입력기를 추가해 줍니다.

![ibus2](README.assets/ibus2.png)



- 그리고 작업표시줄에 있는 'EN'이라고 되어 있는 입력기 선택 아이콘을 눌러서 태극무늬 아이콘으로 변경해주면 이제부터 한/영을 오가며 입력을 할 수 있게 됩니다. 한영키뿐만 아니라 맥에서 사용하는 조합인 Ctrl+Space도 한/영 전환으로 인식하네요.

![ibus3](README.assets/ibus3.png)





#### 키보드 세팅 - fcitx

- https://bebutae.tistory.com/190

```bash
$ sudo apt-get install fcitx -y
$ sudo apt-get install fcitx-hangul -y
$ sudo nano /etc/default/im-config
```

- IM_CONFIG_DEFAULT_MODE=auto를 IM_CONFIG_DEFAULT_MODE=fcitx로 수정해줍니다.

![fcitx](README.assets/fcitx.png)

- Ctrl+x, y, enter를 순서대로 눌러 설정을 저장하고 종료해줍니다. 이제 설치와 기본 셋팅이 끝났습니다.

- 아래 사진과 같이 메뉴를 열고 기본설정의 입력기를 눌러주세요.

![fcitx1](README.assets/fcitx1.png)

- 확인을 누르시고, 예를 눌러 설정을 업데이트하러 이동하겠습니다.

![fcitx2](README.assets/fcitx2.png)

![fcitx3](README.assets/fcitx3.png)

- 최상단의 default를 체크하시고 확인을 눌러주세요.

![fcitx4](README.assets/fcitx4.png)

- 한번 더 확인을 눌러주세요.

![fcitx5](README.assets/fcitx5.png)





### 초음파 세팅

- https://blog.naver.com/dokkosam/222156002480
- https://m.blog.naver.com/roboholic84/220319850312

![KakaoTalk_20210723_110727485](README.assets/KakaoTalk_20210723_110727485.png)

- 우리가 사용한 코드는 ultrasound Test.py 에 들어있음



### PyQt5 + pyWebview

```bash
pi@raspberrypi:~ $ sudo apt-get install python3-pyqt5
pi@raspberrypi:~ $ pip3 install pywebview-3.5-py3-none-any.whl # 다운로드 받은 pywebview 파일명
pi@raspberrypi:~ $ sudo apt-get install python3-pyqt5.qtwebkit # pywebview는 창을 띄우는 엔진으로 qtwebkit or qtwebengine을 필요로함. qtwebengine은 현재 라즈베리파이 버전에선 지원이 안됨
```

- python3-pyqt5를 설치 (pip3 install pyqt5는 먹히지 않았음)
- https://www.piwheels.org/simple/pywebview/ 에서 최신버전 pywebview 다운로드

- https://chmodi.tistory.com/114 를 참고하여 whl 파일 설치
- 설치하고 나서 실행해보니 실행 엔진이 없어서 python3-pyqt5.qtwebkit 설치



### OpenCV



- 210723 작업내역
  - 라즈베리파이 os 설치
  - 한글 설치
  - 초음파 모듈 테스트



- 210803 작업 내역 

  - 오전 

    - pywebview 3.5 버전으로 업데이트 https://chmodi.tistory.com/114 참고함
    - ubuntu 21.04 버전 설치 했었음

  - 오후

    - 면담 결과 다시 라즈베리파이 os로 롤백
    - pywebview 를 통해 간단한 이벤트 처리 성공
    - 기존 코드와 합쳐서 테스트에도 일단 성공
    - 재설치 후에 진행된 라즈베리파이 os에서도 무사히 진행됨
    - 지금까지 진행된 내역 문서화 작업

    