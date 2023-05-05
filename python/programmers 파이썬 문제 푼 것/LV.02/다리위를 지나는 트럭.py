"""
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 
최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 
weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 
트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
"""

#제한조건 다리는 견딜수 있는 하중이 있음
#다리위에 올라 갈 수 있는 차량 수 제한이 있음
#다리 길이에 따라 차량이 건너는 시간이 다름 ex)다리 길이 5는 차량 1대가 다리를 건너는데 걸리는 시간 6초#
from collections import deque
def solution(bridge_length, weight, truck_weights):             # 1 
    answer = 0
    center, right=deque([0 for _ in range(bridge_length)]), deque(truck_weights)
    sum=0

    while right or sum != 0:
        plus= center.popleft()  
        answer +=1
        sum -= plus
        length= 0

        if right and weight >= sum + right[0] and length < bridge_length:
            a= right.popleft()
            center.append(a)
            length +=1
            sum +=a
        else:
            center.append(0)
    return answer


print(solution(2,10,[7,4,5,6]))