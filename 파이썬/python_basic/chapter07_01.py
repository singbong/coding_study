#Chapter07-1
#파이썬 예외 처리의 이해
#예외 종류
#SyntaxError 문법 오류, TypeError ex)int + str 경우, NameError 없는 변수를 선언했을때, IndexError ex)3번 인덱스까지밖에 없는데 4번인덱스
#를 호출하려고 들때 ValuesError, KeyError 문법적으로는 예외가 없지만 코드 실행 프로세스 (단계)발생하는 예외도 중요
#1. 예외는 반드시 처리
#2. 로그는 반드시 남긴다. 개발할떄 로그라는건 증거라고 할 수 있다.
#3. 예외는 던져진다.
#4. 예외 무시

#ZeroDivisionError
#print(100 / 0)

#KeyError
#dic =dict( name = 'Sin', age = 24, length = 176, adrress = "Seoul")
#print(dic['hobby'])

#예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장 (EAPF)

#AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
#print(time.time2()) AttributeError: module 'time' has no attribute 'time2'. Did you mean: 'time'?

#ValueError
#x=[10,20,30]
#x.remove(20)
#print(x)
#x.remove(200) <----ValueError

#FileNotFoundError
#f= open('test.txt') FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

#TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x= [1,2]
# y = (1,2)
# z= 'test'
# #print(x+y)
# a= x+list(y)
# print(a)
# print(a.count(2))
# if 2 in a:
#     print('While문 시작')
#     while 1:
#         print(a.count(2))
#         a.remove(2)
#         if a.count(2) == 0:
#             break
# print(a)
# print()

#예외처리
#try : 에러가 발생 할 가능성이 있는 코드 실행
#except 에러명: 여러개 가능
#except 에러명:
#else : try 블록의 에러가 없을 경우 실행
#finally: 항상 실행
name = ['kim', 'lee', 'park']
#예제1

# try: 
#     z= 'Cho'
#     x= name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except ValueError:
#     print('Not found it! - Occurrd ValueError!')
# else:
#     print('OK! else.')
# print()

#예제2


# try: 
#     z= 'Cho'
#     x= name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception:
#     print('Not found it! - Occurrd ValueError!')
# else:
#     print('OK! else.')
# print()

#예제3


try: 
    z= 'Cho'
    x= name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))
except Exception as g:
    print(g)
    print('Not found it! - Occurrd ValueError!')
else:
    print('OK! else.')
finally:
    print('Ok! finally!')
print()
#예제4
#예외 발생: raise
#raise 키워드로 예외 직접 발생

# try:
#     a= 'Park'
#     if a=='Kim':
#         print('PASS')
#     else:
#         raise ValueError
# except Exception:
#     print('Occurred! Exception')
# else:
#     print("ok! else!")
# finally:
#     print('Done')

