"""
선택정렬의 경우 O(n^^2)의 시간 복잡도를 가진다.


"""


array= [7,5,9,0,3,1,6,2,4,8]
result= []

for i in range(len(array)-1):
    min_index= i
    for v in range(i+1,len(array)):
        if array[min_index] > array[v]:
            min_index= v
    array[i], array[min_index] = array[min_index], array[i]

print(array)

