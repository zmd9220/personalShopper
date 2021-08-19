import pyzbar.pyzbar as pyzbar
import cv2

# 현재 화면을 캡쳐
cap = cv2.VideoCapture(0)

i = 0
while(cap.isOpened()):
  # 사진의 데이터 읽기
  ret, img = cap.read()

  # 비디오를 제대로 읽었었는지 여부 (사진이 제대로 찍혔는지)
  if not ret:
    continue
  
  # 가져온 화면 데이터를 회색으로 칠하기 - 바코드 인식을 하기 쉽도록
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # 회색 화면을 토대로 바코드를 찾아 해석
  decoded = pyzbar.decode(gray)

  for d in decoded: 
    # 바코드 사각형을 위한 좌표
    x, y, w, h = d.rect

    # 바코드 데이터(숫자)
    barcode_data = d.data.decode("utf-8")
    # 바코드 타입
    barcode_type = d.type

    # 인식한 바코드 부분을 빨간 사각형으로 보여주기 위해 감싸기
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # 해석한 바코드 데이터, 타입을 받아 출력 및 cv 화면에 텍스트로 붙여넣기
    text = '%s (%s)' % (barcode_data, barcode_type)
    print(text)
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

  # 수정된 화면을 다시 띄워주기
  cv2.imshow('img', img)

  # 키 입력 받는 부분
  key = cv2.waitKey(1)
  if key == ord('q'):         # 종료
    break
  elif key == ord('s'):       # 현재 화면을 저장
    i += 1
    cv2.imwrite('c_%03d.jpg' % i, img)

cap.release()
cv2.destroyAllWindows()
