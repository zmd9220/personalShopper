import os.path

file = './status/barcode.txt'  # 예제 Textfile

if os.path.isfile(file):
    print("Yes. it is a file")