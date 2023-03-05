#Chapter04-2
#파이썬 반복문
#for 실습

#코딩의 핵심
#for in <collection>
#   <Loop body>

for v1 in range(10): 
    print('v1 is :', v1)
#range에 10은 무조건 n-1
print()

for v1 in range(1, 11):
    print('v1 is :', v1)
print()

for v1 in range(1, 11, 2):
    print('v1 is :', v1)
print()

#1~1000까지의 합
sum1=0
for v1 in range(1,1001):
    sum1= sum1+ v1
    if v1==1000:
        print(sum1)

print('1 ~ 1000 Sum: ', sum(range(1, 1001)))

print(type(range(1,11))) #range형
print()

#1부터 1000까지 4의 배수의 합을 구하시오.

sum2=0
for v1 in range(0, 1001, 4):
    sum2= sum2+ v1
    if v1==1000:
        print(sum2)

print('1 ~ 1000 Sum: ', sum(range(0, 1001, 4)))
print()

#Iterables 자료형 반복
#문자열, 리스트, 튜플, 집함, 사전(딕셔너리)
#iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

#예제1

names = ['Kim', 'Park', 'Cho', 'Lee', 'Sin', 'Choi']

for v in names:
    print('Name is :', v)
print()

#예제2
lotto_numbers = [11 , 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print('Current number :',n)
print()

#예제3
word = 'Beautiful'

for s in word:
    print('word: ', s)

print()

#예제4

my_info =dict(
    name = 'Lee',
    Age = 33,
    City = 'Seoul'
)

for a in my_info:
    print(my_info.get(a))

for v in my_info.items():
    print(v)

#예제5
name = 'FineApple'

for n in name:      #isupper 대문자이냐? 
    if n.isupper():
        print(n)
    else:
        print(n.upper) #upper 대문자 만들어주는 메소드

print()

"""name2 = ''
for i in name:
    name2 =name2 + i.capitalize()
print(name2)
"""

#break문  이후 쓰잘데기 없는 즉 의미 없는 반복을 탈출 시킬 수 있다.

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for i in numbers:
    if i==7:
        print('Found')
        break
    else:
        print('Not Found')


#continue

lt= ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool: #자료형을 대조할때는 is를 쓴다.
        continue        #해당하는 조건이 나오면 skip을 시킴.
    print(type(v))
    print(True*3) # True는 1로 간주
print()

#for-else (파이썬에만 있음)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for i in numbers:
    if i == 49:
        print('FOUND: 49')
        break
else:                     #for문 안에 조건에 모든 반복을 수행 하였을때 리턴이 없으면 마지막으로 else문이 실행된다.
    print('Not Found : 49')

   
#구구단 출력

for i in range(2,10):
    for a in range(1,10):
        print('{:4d}'.format(i*a), end='')
    print()

print()

#변환 예제

name2= 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('tuple', tuple(reversed(name2)))
print('set', set(reversed(name2))) 



