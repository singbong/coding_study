#Chapter03-3
#파이썬 리스트(List)
#자료구조에서 중요
#리스트 자료형 (순서o ,중복o, 수정o, 삭제o)

#선언
a= []
b= list()
c= [70, 75, 80, 85]
print(len(c)) #string형과 똑같이 카운팅
d= [1000, 10000, 'Ace', 'Base', 'Captine']
e= [1000, 10000, d]  #리스트 안에 리스트를 넣을 수 있다.
f= [21.42, 'footbar', 3, 4, False, 3.14159]

#인덱싱 = 원하는 데이터를 꺼내오는 과정

print('>>>>>')
print('d -', type(d), d)
print('d - ', d[1])
print('d - ', d[0]+ d[1]+ d[1]) # 10000+10000+ 1000 이나 온다
print('d - ', d[-1])
print('e - ', e[-1][-1]) #-1에 해당하는 리스트에 -1 값을 호출
print('e - ', list(e[-1][-1]))

#슬라이싱
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][-1][0:2]) #-1에 해당하는 list에 -1인 captine에 0번 인덱스부터 1번 인덱스까지 호출하라

#리스트 연산
print('>>>>>>>')
print('c+d ', c+d)
print('cx3: ', c*3)
print("Test + c[0]=", 'Test' + str(c[0]))

#값 비교
print(c== c[:3] + c[3:])

# Identitiy(id)

temp = c
print(temp, c)
print(id(temp), id(c)) #같은 집주소를 나타내고 있따

#리스트 수정, 삭제
print('>>>>>>>')  #c= 70 75 80 85
c[0] = 4
print('c - ', c)
c[1:2]= ['a', 'b', 'c'] #1번 인덱스 2번 인덱스를 a, b, c로 교체
print(c)
c[1] = ['a', 'b', 'c'] #50번줄 코드는 원소로 교체 되지만 52번줄 코드는 리스트로 교체된다.
print(c)
c[1:3] = []
print(c)
del c[2] #삭제
print(c)
print()


#리스트 함수
a= [5,2,3,1,4]

a.append(10)    #맨 뒤에 추가
print('a - ', a)
a.sort()           #오름 차순으로 순서 정렬
print('a - ', a)
a.reverse()        #sort의 반대 순서로 정렬
print('a - ', a)
print('a - ', a.index(3), a[3]) # a.index는 3이 몇번째 인덱스가 포함되어있는지, a[3]은 3번 인덱스에 뭐가 들어있는지.
a.insert(2, 7) #인덱스 2번 자리에 7을 삽입할거야
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[6] 데이터의 갯수가 많아지면 살상 이방법은 비효율적이며 거의 불가능에 가깝다.
a.remove(10) #10의 원소를 특정해서 삭제한다.
print('a - ', a)
print('a  - ', a.pop()) # 기존의 리스트에서 마지막 인덱스에 해당하는 원소를 가져오고 나머지 원소들로 다시 구성해서 나오는 것 = 마지막 하나가 줄어서 나옴
print('a - ', a) #lifo  last in first out
print('a - ', a.count(4)) #4의 갯수가 한개있다.
ex= [8, 9]
a.extend(ex)
print('a - ', a)

#삭제 : remove, pop, del

sibal= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sibal.reverse()
sibal.sort()
print(sibal)

sibal[:1] = [[11,12,13]]
print(sibal)
sibal= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sibal[0] = [11,12,13]
print(sibal)

#반복문 활용

while sibal:
    print(sibal.pop())











