#Chapter06-3
#파이썬 패키지
#패키지 작성 및 사용법
#파이썬은 패키지로 분할 된 개별적인 모듈로 구성
#상대 경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용
#__init__.py :Python 3.3 부터는 없어도 패키지로 인식 ->단, 하위 호환을 위해 작성 추천



#예제1
import sub.sub1.module1 # 같은 경로에 있을 때는 import로 모듈을 가져올 수 있다.
import sub.sub2.module2

#사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()


print("\n\n\n")
#예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 #a2로 치환

module1.mod1_test1()
module1.mod1_test2()
print()

m2.mod2_test1()
m2.mod2_test2()
print()
#예제3

from sub.sub1 import * # <---sub에 sub1 패키지에 모듈들을 모두 불러오는것 왠만하면 사용하지말 것 필요없는 것 까지 불러오면 비효율
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()
module2.mod2_test1()
module2.mod2_test2()
print()
#예제4  sub3을 만들고 거기에 module_test를 추가한다음 사용해보기

from sub.sub3 import tm as m3

print(m3.add(19, 5))
print(m3.power(2, 10))
print(m3.divide(100, 10))

