"""
퀵정렬은 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법입니다.
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나입니다.
병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브라러리의 근간이 되는 알고리즘입니다.
가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터로 설정합니다.

퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가집니다.
하지만 최악의 경우 O(N^2)의 시간 복잡도를 가집니다.
    첫 번째 원소를 피벗으로 삼을때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행하면 어떻게 될까요?
"""
array= [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫 번째 원소
    left= start + 1
    right =end
    while(left <= right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= right and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right >= left and array[right] >= array[pivot]):
            right -= 1
        if(left > right): #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right -1)
    quick_sort(array, right +1,end)

quick_sort(array, 0, len(array)-1)
print(array)


#파이써닉하게 짠 코드#


def quick(array):
    if len(array) <= 1:
        return array
    pivot= array[0]
    array= array[1:]

    #간편하게 컴프리헨션 사용#
    left = [ x for x in array if pivot >= x]
    right = [ x for x in array if pivot < x]

    return quick(left) + [pivot] + quick(right)

print(quick(array))
