from bisect import bisect_left , bisect_right 

def count_by_range(a, left_value, right_value):
    return bisect_right(a, right_value)- bisect_left(a, left_value)


a= [1,2,3,3,3,3,4,4,8,9]

#값이 4인 데이터의 갯수
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력 
print(count_by_range(a,-1,3))