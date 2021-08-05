# Clova Face Recognition

***

### CFR API란?

* Clova Face Recognition API(이하 CFR API)는 이미지 데이터를 입력받은 후 얼굴 인식 결과를 JSON 형태로 반환합니다. CFR API는 이미지에 있는 얼굴 인식하여 분석 정보를 제공하는 얼굴 감지 API와 닮은 연예인을 알려주는 유명인 얼굴 인식 API를 제공합니다. CFR API는 HTTP 기반의 REST API이며, 사용자 인증(로그인)이 필요하지 않은 비로그인 Open API입니다.



### 사전 준비사항

1. [애플리케이션 등록하기](https://developers.naver.com/apps/#/wizard/register)를 통해 앱 등록 페이지로 이동합니다.
2. **사용 API**에서 **얼굴인식**(CFR API)을 선택합니다.
3. **비로그인 오픈 API 서비스 환경**에 **WEB 설정**을 추가하고 웹 애플리케이션의 **웹 서비스 URL**을 입력합니다.
4. **등록하기** 버튼을 클릭합니다. 버튼을 클릭하면 **내 애플리케이션** 메뉴로 이동하며 방금 등록한 앱의 정보가 화면에 표시됩니다. 이 페이지에서 **Client ID**와 **Client Secret** 정보를 확인할 수 있습니다.



### 구현 예제 (Python)

```python
import os
import sys
import requests
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
# url = "https://openapi.naver.com/v1/vision/face" // 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" // 유명인 얼굴인식
files = {'image': open('YOUR_FILE_NAME', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)
```



***

##### 참고 페이지

https://developers.naver.com/docs/clova/api/CFR/API_Guide.md
