#Chapter06-1
#파이썬 클래스
#OOP(객체 지향 프로그래밍). self, 인스터스 메소드, 인스턴스 변수

#클래스 and 인스턴수 차이 이해
#네임 스페이스 : 객체를인스턴스화 할 때 저장된 공간 __dict__
#클래스 변수: 직접 접근 가능, 공유
# 인스턴스 변수: 객체마다 별도 존재

#예제1

class Dog(): #object 상속
    #클래스 속성
    species = 'animal'   #클래스 변수

    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name             
        self.age = age
#클래스 정보

print(Dog)

#인스턴스화

a= Dog('mikky', 2)
b = Dog("baby", 3)
c= Dog('mikky', 2)

#비교

print(a==b, id(a), id(b), id(c))
print()
#네임 스페이스

print('dog1', a.__dict__)
print('dog1', b.__dict__)
print()
#인스턴스 속성 확인

print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species) #first dog는 클래스 변수임으로 공유하고있다.
print()
#예제2
#self의 이해
class SelfTest:       #__init__ 이 없는 이유는 존재 하지 않을때 파이썬은 내부적으로 알아서 정의를 하기때문 위에 코드 같은 경우는 name이나 age 변수가 필요 하기떄문에 만든것
    def func1():            #메소드를 생성했는데 self가 없다 이것은 클래스 메소드로 본다.
        print('Func1 called')
    def func2(self):   #self가 붙은 것은 인스턴스 메소드입닏.
        print(id(self))
        print('Func2 called')
    


f= SelfTest()
#print(dir(f))
print(id(f))
#f.func1() 예외
f.func2()

SelfTest.func1() #클래수 메소드로 보기때문에 SelfTest 클래스선언해서 불러와야한다, func2는 self가 있으므로 class를 인스턴스화시킨 f로 호출가능
# SelfTest.func2() 이상태에서는 에러가 나지만 인스턴스화 시킨 f를 넣는다면 호출이 된다.

print()
#예제3
#클래스 변수, 인스턴스 변수
class WareHouse:
    #클래스 변수 
    stock_num = 0 #재고
    
    def __init__(self, name):
        #인스턴스 변수
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Lee')
user2 = WareHouse("Cho")
print(WareHouse.stock_num)
print()

print(user1.name)
print(user2.name)
print(user1.__dict__)
print()
print(user2.__dict__)
print()
print(WareHouse.__dict__) # stock_num은 클래스 변수이므로 공유하니까 user.__dict__ 에도 나와야 하는거 아닌가요?
print()
print(user1.stock_num) #근데 파이썬은 또 이렇게는 호출이 가능 user1__dict__에 없을 때는 자기가 포함된 WareHouse의 클래스에서 자기가 알아서 가져옴
print()
del user1
print(WareHouse.__dict__)
print()

#예제4
class Dog2(): #object 상속
    #클래스 속성
    species = 'firstdog'   #클래스 변수

    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name             
        self.age = age
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def bark(self, sound):
        return'{} says {}!'.format(self.name, sound)

#인스턴스 생성

c= Dog2('Gunho', 4)
#메소드 호출
print(c.info())
#메소드 호출
print(c.bark('Meow Meow'))
d= Dog2('seoung hun', 3)
print(d.bark('Wal Wal'))




