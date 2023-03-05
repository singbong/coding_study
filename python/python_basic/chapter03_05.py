#Chapter03-5
#딕셔너리 Dictionary
#범용적으로 가장 많이 사용 (JSon)
#딕셔너리 자료형 (순서o, 키 중복X, 수정o, 삭제o)

#선언 

a = {'name' : 'Kim', 'Phone' : '01095136634', 'birth' : '000225'}  #딕셔너리 안에 , 'name' : 'Lee' <<중복 이므로 말이 안됌   {key : value}
b = {0: 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]} #Key만 존재한다면 Value 는 어떠한 형태든 상관 없음
d= \
{
    'Name': 'SIN',
    'City': 'Seoul',
    'Age' : '24',
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'SIN'),
    ('City' , 'Seoul'),
    ('Age' , '24'),
    ('Grade' , 'A'),
    ('Status' , True)
])                        #리스트 안에 튜플의 형태로 넣어줘야 하기때문에 :대신, 으로 바꾸어 줘야한다. d=e이다

f= dict(
    Name = 'SIN',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

#출력
#print('a - ', a['name1']) 이것은 name key는 있지만 name1이라는 키는 없기 때문에 에러가난다
print('a - ', a.get('name1')) #key의 명명이 잘못되어도 get은 에러가 나오지 않고 None으로 값이 출력된다
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

#딕셔너리 추가
a['adress'] = 'seoul' #adress인 key와 seoul인 value를 dict에 추가
print('a - ', a)
a['rank'] = [1, 2, 3] #리스트도 추가 가능
print('a - ', a)

#딕셔너리 길이
print('a - ', len(a))     #len은 여기서 key의 갯수를 의미
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

#dict_keys , dict_values, dict_items : 반복문(_itter_) 에서 사용가능

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print()

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print()


print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print()
print('a - ', list(a.values()))

print('a - ', a.items()) # key와 valuse가 리스트 안의 튜플의 형태로 불러온다.
print('a - ', list(a.items()))
print()

#딕셔너리 삭제
print('a - ', a.pop('name'))
print('a - ', a)

print('cpop - ', c.pop('arr'))
print('c - ', c)
print()

print('f - ', f.popitem()) #아무거나 임의로 하나 뺀다 추첨기 같은걸 만들때 사용하면 된다.
print('f - ', f)
print()

print('a - ', '000225' in a.values()) #a 딕셔너리에 000225라는 valuse가 있어? 

#수정

a['test'] = 'test_dict' #추가
print('a - ', a)

a['adress'] = 'dj' #adress의 value를 dj로 교체
print('a - ', a)

a.update(birth='910904') #103이랑 같은 방법
temp=dict(adress = 'Busan')

a.update(temp)
print('a - ', a)

key1 =dict(
    name = 'Sin',
    Age = 33,
)


#values값으로 key 찾는 방법

print(list(a.keys())[list(a.values()).index('910904')])

print('910904' in list(a.items()))

print(a.get('birth'))

print(a[1:3])