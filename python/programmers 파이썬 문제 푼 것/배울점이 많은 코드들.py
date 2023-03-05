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