"""
특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘입니다.
    계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능합니다.
데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K)를 보장합니다.

"""
array= [7,5,9,0,3,1,6,2,9,1,4,8,5,2]
result= [0 for _ in range(max(array)+1)]

for i in array:
    result[i] +=1

for i in range(len(result)):
    for v in range(result[i]):
        print(i, end=' ')