# django 사용법

가상환경 설정방법 

```bash
가상환경을 만든다
python -m venv venv

가상환경을 실행시킨다
source venv/Scripts/activate
```

![Untitled](Readme.assets/Untitled-1628213460255.png)

(venv) 가 뜨면 제대로 가상환경이 셋팅된것.

필요한 패키지 import

```bash
장고는 필요한 패키지들의 리스트들을 만들어둘수 있다.(requirements.txt)
거기서 쓰여져있는대로 패키지들을 import한다
pip install -r requirements.txt

현재 설치된 패키지들을 확인한다.
pip freeze
```

![Untitled 1](Readme.assets/Untitled 1-1628213470443.png)

가상환경과 Django환경이 동일함을 알수있다.

DB 설정

```bash
미리 설정해둔 장고 설정에따라 설계서를만든다.
python manage.py makemigrations

설계서대로 모델을 설정
python manage.py migrate

모델(빈꽉) 에 더미데이터를채워넣는다
python manage.py loaddata dummydatalist.json

python manage.py loaddata dummystock.json
```

장고 서버 실행

```bash
python manage.py runserver
```

![Untitled 2](Readme.assets/Untitled 2-1628213484628.png)



## 더미데이터

* fixtures/dummydatalist.json <= 전체 상품 더미 데이터

* fixtures/dummystock.json <= 재고 더미 데이터 

### 상품 카테고리별 사이즈 분류표

| Name       | Column                  | 열       |
| ---------- | ----------------------- | -------- |
| 악세서리   | 999                     | freesize |
| 상의(남성) | 90, 95, 100, 105, 110   | S ~ XL   |
| 상의(여성) | 44, 55, 66, 77, 88      | XS ~ XL  |
| 하의(남성) | 28, 30, 32, 34, 36, 38  | S ~ XL   |
| 하의(여성) | 24, 26, 28, 30, 32, 34  | XS ~ XL  |
| 신발(여성) | 230, 240, 250, 260, 270 |          |
| 신발(남성) | 250, 260, 270, 280, 290 |          |

## 문제해결

* CORS 도메인 문제 해결 (django에서 보내주는 정보 vue에서 오류 없이 읽기)

[https://velog.io/@gomdori5505/CORS-도메인-문제-해결](https://velog.io/@gomdori5505/CORS-%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0)

[https://oen-blog.tistory.com/46]

![Untitled](Readme.assets/Untitled.png)

* SQLite does not support JSONFields 해결하기

> https://www.sqlite.org/download.html
>
> 위 페이지로 접속하여 본인 환경에 맞는 파일 다운로드
>
> https://code.djangoproject.com/wiki/JSON1Extension
>
> 다운로드 받은 파일 위 페이지 참고하여 본인 환경에 맞는 경로로 넣어주기



