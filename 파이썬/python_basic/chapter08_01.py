#Chapter08-1
#파이썬 내장(Built-in) 함수
#자주 사용하는 함수 위주로 실습
#사용하다보면 자연스럽게 숙달
#str(), int(), tuple() 형변환 이미 학습

#절대 값
#abs()
#map filter enumerate 중요
print(abs(-3))

#all, any : iterable 요소 검사(참, 거짓)
print(all([1,2,3])) # and (모두가 참이여야 참, 하나라도 거짓이면 거짓)
print(any([1,2,0])) # or (하나라도 참이면 참)

#chr: 아스키 -> 문자, ord: 문자 -> 아스키

print(chr(1))
print(ord('C'))

#enumerate : 인덱스 + iterable 객체 생성
for i, name in enumerate(['abc','bcd','efg']):  #i는 인덱스를 name은 실제 값을 나타낸다.
    print(i, name)

#filter: 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1,-3,2,0,5,-8])))

def conv_name(x):
    return x == '신'

print(list(filter(conv_name, ['Kim', 'Sin', 'kim', 'Lee', 'Cho'])))


#id : 객체의 주소 값 (레퍼런스) 반환

print(id(int(5)))
print(id(4))

#Len:요소의 길이 반환

#max, min: 최댓값, 최솟값

print(max([1,2,3]))
print(max('pyhthonstudy'))

#map: 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,2,0,-5,6])))

#pow: 제곱값 반환

print(pow(2,10))
print()
#range: 반복 가능한 객체(Iterable)반환

print(range(1,10,2))
print(list(range(1,10,2)))
print()
#round : 반올림

print(round(6.5781, 2))# 6.5781을 소수점 두번째 자리에서 반올림
print(round(5.6))
print()

#sorted: 반복 가능한 객체(Iterable): list tuple set dictionary
"""
sort() 메소드: 리스트를 직접 정렬하여 변경합니다.
sorted() 함수: 정렬된 새로운 리스트를 반환합니다.

# sort() 메소드 사용
a.sort()

# sorted() 함수 사용
b = sorted(a)

"""
print(sorted([6,7,4,3,1,2]))

a= sorted([6,7,4,3,1,2])
print(a)

#sum: 반복 가능한 객체 (ITerable) 합 반환
print(sum([7,8,9,10]))
print(sum(range(0,101,2)))

#type: 자료형 확인
print(type(3))
print(type(())) #튜플

#zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환

print(list(zip([10,20,30],[40,50,60]))) # 결과 값 [(10, 40), (20, 50), (30, 60)]

print(list(zip([10,20,30],[40,50]))) #짝이 맞는 것만 반환[(10, 40), (20, 50)]


    
#map filter 추가 설명
def makeDouble(number):
    return number*2


sample = [1,2,3,4,5]
result =map(makeDouble, sample)  #앞에 인자는 sample 을 어떻게 정희 해줄 것인지 결정 하는 
#함수가 올 수 있음 반환 형태가 list가 아님 그러므로 형변환 해줘야함
print(list(result))

