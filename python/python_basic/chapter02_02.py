#chapter02-2
#파이썬 완전 기초
#파이썬 변수

# 기본 선언
n=700

#출력
print(n)
print(type(n))
print()
#동시 선언
x=y=z=700
print(x,y,z,)
print()
#선언
var=75

#재선언
var = "change value"

#출력
print(var)
print(type(var)) #int형태의 var에 string 형태의 값을 입력하여 str형태의 변수로 변경
print()

#object reference
#변수 값 할당 상태
#1. 타입에 맞는 오브젝트 생성
#2. 값 생성
#3. 콘솔 출력


#예1)
print(300)
print(int(300))

#예2)
# n->777
n=777
print()
print(n, type(n))
print()
m=n
#m->777<-n
print(m, n)
print(type(n), type(m))

m=400
print(m, n)
print(type(n), type(m))
print()

#id(identitiy) 확인 : 객체의 고유 값 확인

m=800
n=600

print(id(m))
print(id(n))
print(id(m) == id(n))        #서로 다른 주소이기 때문에 false가 뜸
print()                        

#같은 오브젝트 참조
m=800
n=800

print(id(m))
print(id(n))
print(id(m) == id(n))    #c언어 같은 경우는 해당 결과 값이 같아도 값이 저장된 주소가 다르기 떄문에 false로 뜨지만 파이썬은 알아서 판단해서 중복 되지 않게 값이 저장됌
print()

#다양한 변수 선언
#Camel Case: numberOfCollegeGraduates    -> Method
#Pascal Case: NumberOfCollegeGraduates -> Class 선언 할때 보통 사용
#Snake Case: number_of_college_graduates

student_grade=3 #스네이크 케이스

StudentGrade=3 #파스칼 케이스 (이것을 변수로 선언 하는 것은 좋은 방법이 아니다 하지말자)

studentGrade=3 #카멜 케이스

#허용 하는 변수 선언 법
age=1
Age=2
aGe=3
AGE=4
a_g_e=5
_age=6
age_=7
_AGE_=8   #특수문자나 숫자로 시작하는 변수는 에러가난다 *숫자는 스네이크 케이스로 선언하도록 하자 

#예약어는 변수명으로 불가능  for while class...etc는 변수 명으로 선언시 에러가 남










