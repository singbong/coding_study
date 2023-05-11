array= [7,5,9,0,3,1,6,2,4,8]


for i in range(len(array)-1):
    min_index= i
    for v in range(i+1, len(array)):
        if array[min_index] > array[v]:
            min_index=v
    array[min_index], array[i] = array[i], array[min_index]

print(array)
        