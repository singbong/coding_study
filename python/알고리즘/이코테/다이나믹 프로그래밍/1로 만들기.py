"""
정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.
1. X가 5로 나누어 떨어지면, 5로 나눕니다.
2. X가 3로 나누어 떨어지면, 3로 나눕니다.
3. X가 2로 나누어 떨어지면, 2로 나눕니다.
4. X에서 1을 뺍니다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 합니다. 
연산을 사용하는 횟수의 최솟값을 출력하세요.
예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값입니다.

26 -> 25 -> 5 -> 1

"""
#다이나믹 프로그래밍 메모이제이션의 상향식(바텀업) 방식#
x= int(input())

d= [0]*(x+1)

for i in range(2, x+1):
    d[i]= d[i-1] +1

    if i%5==0:
        d[i]= min(d[i], d[i//5]+1)
    elif i%3==0:
        d[i] = min(d[i], d[i//3]+1)
    elif i%2== 0:
        d[i]= min(d[i], d[i//2]+1)

print(d[x])

#객체지향#
x= int(input())

class MakeOne():
    d= [0]*(x+1)
    def __init__(self, x):
        self.x= x

    def times(self):
        for i in range(2, x+1):
            MakeOne.d[i]= MakeOne.d[i-1] +1

            if i%5==0:
                MakeOne.d[i]= min(MakeOne.d[i], MakeOne.d[i//5]+1)
            elif i%3==0:
                MakeOne.d[i] = min(MakeOne.d[i], MakeOne.d[i//3]+1)
            elif i%2== 0:
                MakeOne.d[i]= min(MakeOne.d[i], MakeOne.d[i//2]+1)
        return MakeOne.d[self.x]
    
result= MakeOne(x)
print(result.times())




