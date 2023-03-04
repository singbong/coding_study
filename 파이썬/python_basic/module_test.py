#모듈 사용 실습

import sys
# C:\Users\Sin\Desktop\math
print(sys.path)
print()
print(type(sys.path))
print()
#sys.path.append(r'C:\Users\Sin\Desktop\math') #sys가 리스트형이므로 append를 활용하여 해당 주소 파일을 불러오기

#print(sys.path)

#import test_module

#모듈 사용

#print(test_module.power(10,3))

import chapter06_02

print(chapter06_02)
print()

data = dict( name = 'Sin', age = 24, length = 176, adrress = "Seoul")

print(tuple(data.items())) #리스트 안에 튜플 형태로 나옴.
print()

def Test(*abc):     #*이 없고 Lee만 있다고하면 한글자씩 출력
    for i in enumerate(abc):   #i는 인덱스 0번부터 시작 v는 실제 값을 의미
        print('{}'.format(i))

Test('Lee', 'Park', 'Sin')

def Test2(**abc):
    for i in abc.keys():
        print('{}'.format(i), abc.get(i) )

Test2(name = 'Sin', age = 24, length = 176, adrress = "Seoul")













