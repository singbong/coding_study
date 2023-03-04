#Chpater03-6
#집합 특징
#집합 자료형(순서X, 중복X)

#선언

a= set()
b= set([1, 2, 2, 2, 3, 4]) #([1, 2, 3, 3, 3,4]) 3은 한번만 나옴 중복 x
c= set([1, 4, 5, 6])
d= set([1, 2, 'Pen', 'Cap', 'Plate'])
e= {'foo', 'bar', 'baz', 'qux'} #키가 : 밸류 형태가 아니면 집합으로 인식
f= {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', a)
print('b - ', b)
print('c - ', c)
print('d - ', d)
print('e - ', e)
print('f - ', f)
print()

#튜플 변환(set -> tuple)
t= tuple(b)
print('t - ', t)
print()
print('t - ', t[0], t[1:3])


#리스트 변환 (Set->List)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

#길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))       #원소 갯수 만큼 나옴

#집합 자료형 활용

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2=', s1 & s2) # &는 교집함
print('s1 & s2=', s1.intersection(s2)) # 49번줄 코드와 동일

print('s1 | s2= ',s1 | s2) # |는 합집함
print('s1 | s2= ',s1.union(s2))

print('s1 - s2= ',s1 - s2) # 차집함
print('s1 | s2= ',s1.difference(s2))

#중복 원소 확인

print('s1 & s2 : ', s1.isdisjoint(s2)) #False가 나오면 교집합이 있다 True는 교집합이 없다

#부분 집합 확인
print(s1.issubset(s2)) # s1 < s2?
print(s1.issuperset(s2)) # s1 > s2? 

#추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)


s1.remove(2)  #없는 원소를 삭제하려 할 경우 에러가 난다.
print('s1 - ', s1)

print(list(s1).count(1)) #s1에 일치하는게 있는지 확인 하는 방법

s1.discard(7) #없는 원소를 삭제하려 해도 에러가 나지 않는다. 
print('s1 - ', s1)

s1.clear() #list도 clear 가능
print(s1)

s23=set([1, 2, 3, 4, 5, 6])

s24= list(s23)
print(s24)
s24.reverse()
print(s24)   #집합 안에 숫자들을 내림 차순으로 정렬 하는 방법




