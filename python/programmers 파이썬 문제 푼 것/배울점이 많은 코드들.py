def sumMatrix(A,B):
    # return [list(map(sum, zip(*x))) for x in zip(A, B)]
    return [[i+v for i, v in zip(*x)] for x in zip(A,B)] # 같은 것 
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))



def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))


#삼형제
def solution(number):
    answer = 0
    
    for i in range(0, len(number)):
        for v in range(i+1, len(number)):
            for k in range(v+1, len(number)):
                if number[i] + number[v] + number[k] ==0:
                    answer= answer + 1
                else:
                    continue
    return answer


#비트 연산
"""
& : 두 비트가 모두 1이면 1을 반환하고, 그 외에는 0을 반환합니다. (비트 AND)
| : 두 비트 중 하나라도 1이면 1을 반환하고, 둘 다 0일 때만 0을 반환합니다. (비트 OR)
^ : 두 비트가 서로 다르면 1을 반환하고, 같으면 0을 반환합니다. (비트 XOR)
~ : 비트를 반전시킵니다. 1은 0으로, 0은 1로 변환됩니다. (비트 NOT)
<< : 비트를 왼쪽으로 이동시킵니다. 오른쪽에는 0을 채웁니다.
"""

# print(bin(a & b))  # 0b1000 (AND 연산)
# print(bin(a | b))  # 0b1110 (OR 연산)
# print(bin(a ^ b))  # 0b0110 (XOR 연산)
# print(bin(~a))     # -0b1011 (비트 반전 연산)
# print(bin(a << 1)) # 0b10100 (왼쪽으로 1비트 이동)
# print(bin(b >> 2)) # 0b0011 (오른쪽으로 2비트 이동)
print(bin(22)[2:])
print(bin(12)[2:])
print(bin(22 | 12)[2:]) # 시벌 몰라서 노가다했네



#아리스토텔레스 체 문제: 소수찾기 코드
def solution(n):
    num=set(range(2,n+1)) #리스트 빼기 리스트는 안되지만 집합 빼지 집합 즉, 차집합이라느 개념이 있기에 굉장히 효율적인 코드

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

def solution(n):
    num= set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num= num - set(range(2*i, n+1, i))
    return len(num)

#위 함수와 아래 함수가 왜 다른건지 도저히 이해가 안갔으니 num-=1 이런식은 num을 업데이트 하는 방식이고 num num-1은 num을 재할당 하는 것이라
# 속도 면에서 차이가 난다고 한다.......... 

"""
num -= set(range(2*i, n+1, i))은 num을 업데이트 하는 것이고, num = num - set(range(2*i, n+1, i))은  
새로운 set 객체를 만들어 num을 재할당하는 것입니다. 
"""

# ex)  [1, 2, 3, 4, 5] 문제 모의고사 코드
def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]
    for i, ans in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if ans == pattern[i % len(pattern)]:
                scores[j] += 1
    max_score = max(scores)
    return [i+1 for i, score in enumerate(scores) if score == max_score]

from itertools import cycle

def solution(answers):
    patterns = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    scores = [0, 0, 0]
    for i, ans in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if ans == next(pattern):
                scores[j] += 1
    max_score = max(scores)
    return [i+1 for i, score in enumerate(scores) if score == max_score]

#리스트 집합 딕셔너리 가변형데이터 이므로 call by reference 가능
#문자열 튜플은 불변형데이터 형식 call by value
