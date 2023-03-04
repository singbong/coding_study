#Chaper08-2
#파이썬 외장 (External) 함수
#실제 프로그램 개발 중 자주 사용
#종류 : sys,pickle, shutil, temfile,time, random

#예제1

import sys
print(sys.argv)

#예제2(강제 종료)
#sys.exit()

#예제3(파이썬 패키지 위치)
print(sys.path)

#pickle : 객체 파일 쓰기/읽기 *
import pickle

# 예제4(쓰기)
f= open("test.obj", 'wb')
obj= {1: 'python', 2:'study', 3:'basic'}
pickle.dump(obj, f)             #파이썬에 사용 할 tn 있는 어떤 객체, class, dictionary, list, tuple 이런 것들을 저장장치에 쓸때 사용하고
#불러올떄 사용 하는 것이 pickle

f.close()
print()
#예제5(읽기)

f= open('test.obj', 'rb')
data= pickle.load(f)
print(data, type(data))
f.close()
print()
#os: 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
#mkdir, rmdir(비어 있으면 삭제), rename

#예제6

import os
print(os.environ)
print()
print(os.environ["USERNAME"])

#예제7(현재경로)
print(os.getcwd())# 파이썬이 실행되고있는 폴더 경로 표시

#time : 시간 관련 처리  ******매우중요
import time

#예제8
print(time.time())

#예제9(형태변환)
print(time.localtime(time.time()))

#예제10 (간단표현)
print(time.ctime())

#예제 11 (형식 표현)
print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))) #가장 많이 사용 되는 방식
#예제12 (시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(2)  #2초 딜레이

#random: 난수 리턴
import random

#예제12
print(random.random())# 0~1 실수 랜덤

#예제 14
print(random.randint(1,45)) # 1~45 사이의 int형 숫자 랜덤
print(random.randrange(1,45)) #1~44사이의 숫자 랜덤

#예제15(섞기)
d= [1,2,3,4,5]
random.shuffle(d)
print(d)

#예제16(무작위 선택)

c= random.choice(d)
print(c)

#webbrowser: 본인 os의 웹 브라우저 실행

import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")


