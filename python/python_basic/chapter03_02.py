#Chapter03-2
#파이썬 문자형
#문자형 중요!!!!

#문자열 생성
str1= "I am python"
str2= 'python'
str3="""how are you"""
str4= '''Thank you'''
print(len(str1),len(str2),len(str3),len(str4))
print()

#빈 문자열
str1_t1= ''
str2_t2= str()  #바로 위 코드와 동일한 코드 좀 더 세련된

print(type(str1_t1), type(str2_t2), "length:", len(str1_t1), len(str2_t2))
print()

#이스케이프 문자사용
#I'm boy

print("i'm boy") #에러가 안난다 하지만 "을'로 바꿀경우 에라가 ㅏㄴ다
print('i\'m boy') # \을 사용하여 바로 뒤 특수문자를 출력한다 이스케이프 방식
print('a \t b') #tab키 눌렀을 떄의 간격 만큼 벌어져 출력
print('a \n b') #\n은 출 바꿈

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'what\'s going on?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1= "click \t start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

#Raw String 출력
raw_s = r'd:\python\test'
print(raw_s)
print()

#멀티 라인
multi_str =\
'''
문자열
멀티라인 입력
테스트
'''                         
print(multi_str)
#멀티 입력
#역슬래시 사용
asdf = \
'asdasdsad' \
'ddddddddd'

print(asdf)
print()

#문자열 연산
str_o1 = 'python'
str_o2= 'apple'
str_o3= 'how are you doing'
str_o4= 'Seoul daejeon busan jinju'

print(str_o1 * 3) #python이 3번 반족해서 출력
print(str_o1 + str_o2) # python apple 출력
print('y' in str_o1) #str_o1에 y가 있어? 라는 함수는 in이다
print('P' not in str_o2)

result = 'm' in str_o1
if result==1: {
    print("포함됌")
}
else: {
    print("포함 안됌")
}
print(type(result))

print()

#문자열 형 변환
print(str(66), type(str(66))) #66은 숫자가아닌 문자열
print(str(10.1)) # 이것또한 10.1은 float형이 아닌 str형
print(str(True), type(str(True)))
print()


#문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha....)

print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s")) #끝글자가 s로 끝났니?
print("replace: ", str_o1.replace("thon", 'Good')) #thon이라는 부분을 Good으로 바꿔줘
print("sorted: ", sorted(str_o1))   #문자열을 받아서 어떤 기준에 맞게 list 형태로 반환한다.
print("split: ", str_o4.split(' ')) #띄어 쓰기를 기준으로 list화 시킨다 wqe
print()

#반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #_iter_ 

#출력
for i in im_str:
    print(i)

#슬라이싱
str_s1 = "Nice Python"


#슬라이싱 연습
print(str_s1[0:3]) #0부터 3-1까지

print(str_s1[5:11]) 
print(str_s1[5:]) #윗줄 코드와 같음
print(str_s1[:len(str_s1)]) #[:]=[0:11]=[:len(str_s1)]
print(str_s1[1:9:2]) #1부터 9까지 불러오는데 2칸씩 띄어서 가져와라
print(str_s1[-5:]) #ython이 출력
print(str_s1[1:-2])
print(str_s1[1::3])
print(str_s1[::-1])

#아스키 코드(또는 유니코드)

a= 'z'
print(ord(a)) #아스키 코드로 보여주는 함수는 ord
print(chr(122))  #char는 아스키 코드 -> 문자로

print("결과 값: ", '{:>20s}'.format(str_s1))














