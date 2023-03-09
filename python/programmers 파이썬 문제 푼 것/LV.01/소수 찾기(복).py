"""
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예

n	result
10	4
5	3

입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
"""
def solution(n):
    num= set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num= num - set(range(2*i, n+1, i))
    return len(num)



print(solution(10))
# 시간이 너무 오래 걸리므로 에라토스테네스의 체라는 방법을 써야한다.
"""
에라토스테네스의 체는 소수를 찾는 알고리즘 중 하나입니다. 5라는 숫자가 있으면 2부터 int(5**0.5) 까지 숫자가 5라는 숫자를 나누었을 때 나누어
떨어지면 5라는 숫자는 소수가 아니고 안나누어 떨어지면 소수이다. 
"""
def solution(n):
    answer = 0
    numbers = list(range(2,n+1)) # 2 3 4 5
    for i in numbers:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer






