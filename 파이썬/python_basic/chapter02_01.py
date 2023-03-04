# chapter02-1
# 파이썬 완전 기초
# print 사용법

#기본 출력 
print('파이썬 시작')
print("파이썬 시작")
print()                 #줄 바꿈     
print("""파이썬 시작""")
print('''파이썬 시작''')
print()

# separator 옵션

print('P','Y','T','H','O','N')

print('P','Y','T','H','O','N', sep='|') #sep은 각 글자마다 해당 문자로 나누니 ex(p|y|h|o|n|)
print('010','9513','6634', sep='-')
print()

#end 옵션
print('welecome to', end=' ') #프린트문은 자동으로 줄바꿈 해주지만 end 옵션이 들어가면 다음 print문과 이어 줄 수 있다.
print('it news', end=' ')
print('web site')
print()

#file 옵션
import sys
print('learn python', file=sys.stdout) #learn python 이라는 내용을 sys.stdout의 파일에 내보낸다.
print()

#format 사용(d,s,f) d는 정수 s는 문자열 f는 실수 digit strin float .... 그 외에는 double 등등 더있다.
print('%s %s' % ('one','two'))  #그전에 c언어 할때 해당 글자의 문자형을 지정 해주고 입력 해주는 방식
print('{} {}'.format('one','2')) #가독성은 바로 윗줄 코드가 더좋다.
print('{1} {0}'.format('one','two')) #인덱스는 0부터 시직이기 때문에 0에 해당하는 two가 먼저 출력된 것

print('%d %d' % (1,2))
print('{1} {0}'.format(1,2))
print()

#%S

print('%10s' % ('nice')) #10자리를 문자열로 사용하겠다고 선언하고 nice를 10칸에 출력
print('{:>10}'.format('nice')) #임의적으로 왼쪽 (>)부터 nice를 출력

print('%-10s' % ('nice')) 
print('{:10}'.format('nice')) 

print('{:_>10}'.format('nice')) #공백을 '_' 이것으로 채운다 ex)________10

print('{:^10}'.format('nice')) #중앙 정령은 '^'이다.

print('{:10d}'.format(345))
print('{:10s}'.format('345')) #문자열은 디폴트가 왼쪽 정령 숫자는 오른쪽 정렬이다.

print('%.5s' % ('python study'))
print('%5s' % ('python study'))

print('{:10.5}'.format("pythonstudy")) #공간은 10개를 가져와서 5개만 나와라

print('{:_^5}'.format('i')) #i를 중앙 정령하고 나머지는 _로 채워라.
print('{:_^5} {:_^5}'.format('i','b'))
print('{:_^5} {:_^5d}'.format('i',5))
print('%s %d' % ('as',5))

#%f
print('%f' % (3.1518954))
print('%1.3f' % (3.123456789)) #소수 셋째자리 까지 출력해라
print('{:1.2f}'.format(3.123456789)) #소수 첫번째 자리 까지 출력하라 

print('%03.2f' % (3.123456789)) # 3자리 수 소수점 자리는 두번째 자리까지 출력 나머지는 0으로 출력
print('%03.1f' % (3.123456789))


print("이것은", '{:?^10s} {:@^10s}'.format('sibal','fuck')) 

print('{:?>100.5s}'.format('python study'))
 