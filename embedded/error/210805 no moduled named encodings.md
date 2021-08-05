# Error

``` 
 Fatal Python error: initfsencoding: unable to load the file system codec ModuleNotFoundError: No module named 'encodings'
```



* 파이썬 버전을 3.5에서 3.8 변경하는 과정에서 생긴 에러 
* 이전의 환경변수를 제거하고 새 파이썬 경로를 환경 변수로 지정하면 해결



1.  이전 버전의 python 환경 변수가 있을 경우 제거한다.

2.  시스템 속성 > 환경 변수 > 시스템 변수 path 선택 후 편집

   ![image-20210805113319154](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210805113319154.png)

3.  새로 만들기(N) 클릭 후 Python 경로 쓰고 확인

   * 경로 찾는 방법

     1.  python 검색 > 파일위치 열기

        ![image-20210805113529098](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210805113529098.png)

        

     2. python 버전 (64-bit) 오른쪽 마우스 클릭 후 속성 > 대상의 경로 복사 후 뒤의 #python.exe 제거 후 붙여넣기

***



