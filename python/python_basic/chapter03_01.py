# Chapter03-1
#숫자형

#파이썬 지원 자료형
"""
int: 정수
float: 실수
complex: 복소수
bool: 불린(true false)
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집함
dict: 사전
"""

#데이터 타입
str1= "python"
bool= False
str2= 'Anaconda'
float_v = 10.0 # 10과 10.0은 다르다 10은 정수 타입 10.0은 float타입
int_v= 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple= (7, 8, 9) # 괄호 없이 7, 8, 9 로 선언 가능 중괄호 대괄호 소괄호 모두 가능
set= {3, 5, 7}



#데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+
-
*
/
// : 몫
%  : 나머지
abs(x): 절댓값
pow(x, y) = x** y x의 y승
"""
#정수 선언
i=77
i2= -14
big_int= 77777777777777799999999999

#정수 출력

print(i)
print(i2)
print(big_int)
print()

#실수 출력
f= 0.99999
f2= 3.141592
f3= -3.9
f4= 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

#연산 실습
i1= 99
i2= 939
big_int1 = 798465132156454321654
big_int2 = 771111222348888
f1 = 1.234
f2 = 3.939

# +
print(">>>>+")
print("i1+i2: ", i1+i2)
print("big_int1+ big_int2: ", big_int1 + big_int2)
print()

# *
print(">>>>*")
print("i1*i2: ", i1*i2)
print("big_int1* big_int2: ", '{:3.1f}'.format(big_int1 * big_int2))
print()

#형 변환 실습
a= 3. #3.0을 의미
b= 6 
c= .7 #0.7을의미
d= 12.7

#타입 출력
print(type(a), type(b), type(c), type(d))


#형변환
print(float(b)) #정수를 실수로 형변환
print(int(c))  #실수를 정수로 형변환
print(int(d))    
print(int(True))   #true는 1을 나타내고 flase는 0을 나타내므로 bool형 이였던 값을 정수로 형 변환하면서 1을 출력
print(int(False))
print(complex(3))
print(complex('3')) #다른 언어였으면 에러가 나는 코드지만 파이썬은 알아서 숫자로 인식해서 코드가 실행돠고 3+0j로 출력된다,.
print(complex(False))
print(complex(True))
print()
#수치연산 함수
print(abs(-7))
x, y = divmod(100,8) # divmod는 몫과 나머지를 출력해주는 함수인다.
print(x, y)
print(pow(5,3), 5**3) #pow(ㅌ,ㅛ)는 ㅌ의 ㅛ 승을 나타내는 함수
print()

#외부모듈

import math      #여러가지 수학적 계산 도구들을 불러오는 것

print(math.pi)
print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정수









