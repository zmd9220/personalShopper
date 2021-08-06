import os
import sys
import requests

client_id = "h_Dm9g2KyYo6TrZtbkMQ"
client_secret = "d9yEBBJ1rU"
url = "https://openapi.naver.com/v1/vision/face"
#files = {'image': open('YOUR_FILE_NAME', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

sys.stdout = open('stdout.txt', 'w')
for i in range(1, 26):
    if i < 10:
        string = '0'+str(i)
    else:
        string = str(i)
    files = {'image': open('../img/{}.jpg'.format(string), 'rb')}
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code

    if(rescode==200):
        print (response.text)

    else:
        print("Error Code:" + rescode)

sys.stdout.close()