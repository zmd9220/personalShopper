# MS Azure

### Azure 환경 구축

* Azure 체험 계정 만들기

  https://azure.microsoft.com/ko-kr/free/

  + Azure 포탈 접속

    https://portal.azure.com/#home

* Conitive Services 계정 만들기
  + 리소스 만들기 선택 > Cognitive Services 검색 > 만들기

***



###  FaceAPI

1. 프로젝트를 진행하기 앞서 홈 디렉터리 아래에 MSFACE 디렉터리를 생성

2. cmd 창에서 cognitive_face 모듈을 설치

   ```bash
   $ pip install cinitive_face
   ```

3. 파이썬 스크립트 작성

   ```python
   import requests
   from io import BytesIO
   from PIL import Image, ImageDraw
   import cognitive_face as CF
   
   KEY = 'KEY' # 자신의 Cognitive Services API KEY
   CF.Key.set(KEY)
   
   BASE_URL = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/' # 자신의 지역에 해당하는 URL
   CF.BaseUrl.set(BASE_URL)
   
   img_url = '/home/pi/MSFACE/im1.jpg' # 이미지 파일의 경로
   faces = CF.face.detect(img_url,True,False,'age,gender') # 중요!
   # detect 함수는 4가지의 매개변수를 갖는다.
   # 첫 번째 인자 : 이미지파일
   # 두 번째 인자 : face_id의 반환 여부
   # 세 번째 인자 : landmarks(눈,코,입 등의 위치)의 반환 여부
   # 네 번째 인자 : 반환할 속성(연령,성별 등)
   
   for face in faces:
       print(face['faceAttributes']) # 터미널 창에 속성값들을 출력
   
   # 인식된 얼굴에 네모 박스 그리는 함수 작성
   def getRectangle(faceDictionary):
       rect = faceDictionary['faceRectangle']
       left = rect['left']
       top = rect['top']
       bottom = left + rect['height']
       right = top + rect['width']
       return ((left, top), (bottom, right))
   
   img = Image.open(img_url) # img 변수에 이미지 파일을 넣어준다.
   draw = ImageDraw.Draw(img)
   for face in faces:
       draw.rectangle(getRectangle(face), outline='red') # 인식된 얼굴들에 네모 박스 쳐주기
   
   img.show() # 이미지 뷰어로 이미지 띄우기
   ```

   * 수정할 것 3가지
     1. KEY
        - Azure 포탈의 홈에서 Cognitive Services를 선택
        - 좌측의 Keys 선택
        - Key 확인
     2. BASE_URL
        - 위의 소스코드는  대한민국 중부의 주소로 설정되어 있다.
     3. img_url
        - 본인 환경에 맞게 수정해주면 된다.

4.  파이썬 스크립트 실행



***

##### 참고 페이지

https://m.blog.naver.com/ljy9378/221463787050

https://m.blog.naver.com/ljy9378/221463790053



