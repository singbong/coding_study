#Chapter04-3
#파이썬 반복문
#While 실습

#While <expression>:
#   <statement(s)>

#예제1

n= 5

while n > 0:
    print(n)
    n= n-1

#예제2
a= ['foo', 'bar', 'baz']

while a:
    print(a.pop())
print()

#예제3
#break, continue
n= 5
while n:
    n= n-1
    if n==2:
        break
    print(n)
print('Loop End')
    
print()
#예제4

m= 5
while m:
    m= m-1
    if m==2:
        continue
    print(m)
print('Loop End')
print()

#if 중첩
#예제5

i = 1
while i<= 10:
    print('i:', i)
    if i==6:
        break
    i=i+1

#while - else 구문

#예제6
n=10
while n>0:                          
    n= n-1
    print(n)
    if n==10:
        break
else:                    #위 반복문을 전부 실행 하였는데 리턴값이 없으면 else문 실행
    print('else out')
print()

#예제7
a= ['foo', 'bar', 'baz', 'qux']
s= 'qux'
i=0

while i<len(a):
    if a[i] == s:
        print('found in list.a')
        break  
    i= i+1
else:
    print(s, 'not found in list.a')
print()
#무한 반복 조심!
#예제8
a= ['foo', 'bar', 'baz']

while 1:
    if not a:
        break
    print(a.pop())


