#Chapter05-1
#파이썬 함수 및 중요성
#피어썬 함수식 및 람다(Lambda)

#함수 정의 방법
#def function_name(parameter):
# code

#예제1
def first_func(w):
    print("Hello, ", w)

word= "Good Boy"

first_func(word)
print()

#예제2
def return_func(w):
    value= "Hello, " + str(w)
    return value

x= return_func('Good boy2')
print(x)

#예제3(다중반환)

def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y, z)
print()
#튜플 리턴

def func_mul2(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return (y1, y2, y3)

q= func_mul2(20)

print(type(q), q, list(q))
print()
#리스트 리턴

def func_list(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return [y1, y2, y3]
e= func_list(30)
print(type(e), e)
print()

#set 리턴
def func_set(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return set([y1, y2, y3])
r= func_set(40)
print(type(r), r, list(r))
print()

#딕셔너리 리턴
def func_dictionary(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return dict( v1= 'y1', v2= 'y2', v3= 'y3')
t= func_dictionary(50)
print(type(t), t, t.popitem())
print()

#중요
#*args, **kwargs 

#*args(언팩킹)
def args_func(*args):  #매개변수 명은 자유 
    for i,v in enumerate(args):
        print('Result {}'.format(i), v)
    print('-------')

args_func('Lee')
args_func('Lee', 'Park', 'Sin')
print()

#**kwargs(언팩킹) 딕셔너리형
def kwargs_func(**args):
    for i in args.keys():
        print("{}".format(i), args.get(i))
    print('---------------')

kwargs_func(name1= 'Lee')
kwargs_func(name1= 'Lee', name2= 'Kim')
kwargs_func(name1= 'Lee', name2= 'Kim', name3= 'Sin')

#전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)
print()

#중첩 함수 함수형 프로그래밍을 할 때 많이 사용되는 방법이다.
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In func')
    func_in_func(num+100)
nested_func(100)
print()
#func_in_func(1000) 이함수는 이전 함수인 nested_func 함수를 호출하지 않았음으로 존재하지 않는 함수이다.

#람다식 예제
#메모리 절약, 가독성 향상, 코드 간결
#함수는 객체 생성 ->리소스(메모리) 할당
#람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
#남발 시 가독성 오히려 감소
"""
def mul_func(x,y):
    return x*y

lambda x,y:x*y #mul_func() 와 리턴값이 같다
"""
#일반적 함수 -> 할당
def mul_func(x,y):
    return x*y
print(mul_func(10,50))
mul_func_var = mul_func
print(mul_func_var(20,50))
print()

#람다 함수 ->할당
lambda_mul_func= lambda x,y:x*y
print(lambda_mul_func(10,50))

def func_final(x, y, func):
    print(x*y*func(100,200))

func_final(10,20, lambda x,y:x*y)
print()






