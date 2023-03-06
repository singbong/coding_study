
def solution(array, commands):
    answer = []
    
    for i in commands:
        print(array[i[0]-1:(i[1])])
        answer.append(sorted(array[i[0]-1:(i[1])])[i[2]-1]) 
        
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[4, 4, 1]]))


