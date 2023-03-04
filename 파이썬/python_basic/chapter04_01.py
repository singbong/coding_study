 #Chapter04-1
 #파이썬 제어문
 #IF 실습

#기본 형식
print(type(True)) #0이 아닌 수, "abc:, [1,2,3,....], (1,2,3,....) 는 True
print(type(False)) # 0,"",[],(),{}... 는 False
print()
#예1

if True:
    print('Good')

#관계 연산자
#>, >=, <, <=, ==, !=
x= 15
y = 10


city = str()
if city:
    print("You are in ", city)
else:
    print('Please enter yout city')
print()

city2 = "Seoul"
if city2:
    print("You are in ", city)
else:
    print('Please enter yout city')

#논리 연산자(중요함)
#and, or, not
a= 75
b= 40
c= 50
print('and: ', a > b and b > c)
print('or : ',a>b or b>c)
print('not: ', not a>b) #a>b 결과가 True임으로 False 출력

#산술, 관계, 논리 우선순위
#산술 > 관계 > 논리
print('e1: ',3+12 > 7+3)
print('32 :', 5+10+3>7+3+20)
print('e3 :', 5+10 > 3 and 7+3 ==10) #and는 논리 > < <= <=는 관계이므로 10>3 and 10==10 --->True and True
print('e4 :,', 5+10>0 and not 7+3 == 10)

score1= 90
score2='A'

#복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2== 'A':
    print('Pass')
else:
    print('Fail')

#예5
id1= 'Vip'
id2= 'Admin'
grade= 'Platinum'

if id1=='Vip' or 'Admin':
    print('관리자 입장')

if id2 == 'Admin' and grade == 'Platinum':
    print('최상위 관리자')
print()

#예6
#다중조건문
num= 70

if num >=90:
    print('A')
elif num>=80:
    print('B')
elif num>=70:
    print('C')
else:
    print('과락')
print()

#중첩 조건문

#예7
grade = 'A'
total = 70

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >=80:
        print('장학금 50%')
    else:
        print('장학금 10%')
else:
    print("장학금 없음")
print()

#in, not in

q= [10, 20, 30]
w= {70, 80, 90, 100}
e= dict(
    name= "Lee",
    city= "Seoul",
    grade= "A"
)
r=(10,12,14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e) #Key만 인식
print("Seoul" in e.values()) #values에 seoul이 있냐
