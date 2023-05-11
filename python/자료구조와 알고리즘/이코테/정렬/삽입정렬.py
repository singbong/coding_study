## 삽입 정렬##
"""
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다.
선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작합니다.

삽입정렬은  O(n^^2)의 시간 복잡도를 가지며
어느정도 정렬이 된 데이터의 경우 시간복잡도는 훨씬 줄어든다.
"""

array= [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for v in range(i-1, -1, -1):
        if array[v+1] < array[v]:
            array[v+1], array[v] = array[v], array[v+1]
        else:
            break 

print(array)










