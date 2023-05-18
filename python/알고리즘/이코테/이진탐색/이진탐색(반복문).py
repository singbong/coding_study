def binary_search(array, target, start, end):

    while start <= end:
        mid= (end + start) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end= mid-1
        else:
            start= mid+1
    else:
        return None
#n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target= list(map(int, input().split()))

array= list(map(int, input().split()))

# 이진 탐색 수행 결과 출력

result= binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result +1)