"""
피보나치 수열: 단순 재귀 소스코드

단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됩니다.

                    f(6)
            f(5)            f(4)
        f(4)    f(3)    f(3)    f(2)
이런 트리 구조를 가지게 되는데 보는 바와 같이 2^n의 시간복잡도를 가지면
반복되는 값이 자주 보이게 된다. 이럴 경우에 너무 비효율적이다.

* 다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있습니다.
 1. 최적부분 구조(Optimal Substructure)
    큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결
 2. 중복되는 부분 문제(Overlapping Subproblem)
    동이한 작은 문제를 반복적으로 해결해야 합니다. 

    다이나믹 프로그래밍의 구현은 일반적으로 두가지 방식(하향식과 상향식)

    
**메모이제이션(Memoization)**
*메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나입니다.
* 한번 계산한 결과를 메모리 공간에 메모하는 기법입니다.
    같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옵니다.
    값을 기록해 놓는 다는 점에서 캐싱(Caching)이라고도 합니다.

"""
## 피보나치 시간 복잡도 2의 n승 구현 방법
def fibo(x):
    if x== 1 or x== 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

##객체지향적으로 코드 짜보기##

class fibo():
    def __init__ (self, x):
        self.x= x

    def finder(self):
        if self.x==1 or self.x==2:
            return 1
        return fibo(self.x - 1).finder() + fibo(self.x - 2).finder()
    
find= fibo(4)
print(find.finder())

## 다이나믹 프로그래밍(메모이제이션)을 통한 피보나치 수열 구현 방법
"""
탑다운(메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식이라고 합니다.
다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식입니다.
    결과 저장용 리스트는 dP 테이블 이라고 부릅니다.
엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미합니다.
    따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아닙니다.
    한번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 할용하지 않을 수도 있습니다.
"""
#피보나치 수열 하향식#
a= int(input())

d= [0]*(a+1)

def fibo(x):
    if x==1 or x== 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x]= fibo(x-1)+fibo(x-2)

    return d[x]

print(fibo(a))

##객체지향적 코딩 짜보기##
class fibo():
    d= [] # 클래스 변수
    def __init__ (self, x):
        self.x= x

    def finder(self):
        if self.x==1 or self.x==2:
            return 1
        if fibo.d[self.x] != 0:
            return fibo.d[self.x]
        fibo.d[self.x]= fibo(self.x - 1).finder() + fibo(self.x - 2).finder()
        return fibo.d[self.x]

a= int(input())
fibo.d= [0]*(a+1)  #클래스 변수 초기화
find= fibo(a)
print(find.finder())


##상향식##

d= [0]*100

d[1]=1
d[2]=1
n= int(input())

for i in range(3,n+1):
    d[i]= d[i-1]+ d[i-2]

print(d[n])

##객체지향적 프로그래밍 짜보기

class fibo():
    d= []
    def __init__(self, x):
       self.x= x
    def finder(self):
        fibo.d[1]=1
        fibo.d[2]=1

        for i in range(3, self.x + 1):
            fibo.d[i]=fibo.d[i-1]+fibo.d[i-2]

        return fibo.d[self.x]
    
a= int(input())
fibo.d= [0]*(a+1)

find= fibo(a)
print(find.finder())

##메모이제이션을 이용한 상향식 하향식 방법을 사용하여 피보나치 함수를 생성하면 2^n에서 n으로 시간복잡도 감소##










