#Chapter03-4
#파이썬 튜플
#리스트와 비교 중요
#튜플 자료형(순서o, 중복o, 수정x, 삭제x) #불변

#선언

a= ()
b= (1)

print(type(b), type(a)) #이런 경우 a는 튜플 b는 인트 타입으로 인식한다
b= (1,) #원소가 하나인 경우 ,를 찍어줘야 튜플로 인식한다
print(type(b), type(a)) #a, b 둘다 튜플 타입
c= (11, 12, 13, 14)
d= (100, 10000, 'Ace', 'Base', 'Captine')
e= (100, 10000, ('Ace', 'Base', 'Captine')) #list와 똑같이 튜플 안에 튜플 가능


#인덱싱
print('>>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1])) #튜플의 특성이 사라지고 list의 특성으로 변환

#수정 X
#d[0] = 1500

#슬라이싱
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

#튜플 연산
print('c+d', c + d)
print('c*3', c*3)

#튜플 함수
a= (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

#팩킹 & 언팩킹 (Packing, and Unpacking)


#팩킹

t= ('foo', 'bar', 'baz', 'qux') #<<<팩킹이라고한다
print(t)
print(t[0])
print(t[-1])

#언팩킹1 매우 중요
(x1,x2,x3,x4)=t

print('type : ', type(x1), type(x2), type(x3), type(x4))
print(x1,x2,x3,x4)

#팩킹 & 언팩킹
t2= (1, 2, 3)
t3= (4,)
(x1, x2, x3) = t2
(x4, x5, x6) = (4, 5, 6)


print(t2)
print(t3)
print(x1,x2,x3,x4)# 언팩킹
print(x4,x5,x6)#언팩킹

#시퀀스의 형태면 슬라이싱 무조건 가능 [:]


















