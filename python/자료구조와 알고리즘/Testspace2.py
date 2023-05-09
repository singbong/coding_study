array= [7,5,9,0,3,1,6,2,4,8]

def quick(array):
    if len(array) <= 1:
        return array

    pivot= array[0]
    array=array[1:]

    left = [x for x in array if x < pivot]
    right = [x for x in array if x >= pivot]

    return quick(left) + [pivot] + quick(right)

print(quick(array))

