"""
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
 예를 들어 수열 {1,1,2,2,2,2,3}이 있을때 x=2라면, 현재 수열에서 2인 원소가 4개이므로 4를 출력합니다.

단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받습니다.
"""

from bisect import bisect_left, bisect_right

n, m= map(int, input().split())
array= list(map(int, input().split()))

result= bisect_right(array, m)- bisect_left(array, m)

print(result)

