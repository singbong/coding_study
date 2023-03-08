"""
제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 
있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
* nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
* nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

  nums	    result
[1,2,3,4]	  1
[1,2,7,6,4]   4
"""
def solution(nums):
  numbers = list()
  for i in range(0, len(nums)-2):
      for v in range(i+1, len(nums)-1):
          for k in range(v+1, len(nums)):
            numbers.append(nums[i]+nums[v]+nums[k]) #스택을 이용한 세개의 수를 더한 경우의 모두 출력
  result = 0
  for i in numbers:         #소수 판별 코드
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1): #에라토스테네스의 체를 이용한 소수 판별
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result += 1
  return result
#어떤 자연수 n이 소수가 아니라면, n은 n = a * b (단, a <= b) 형태로 나타낼 수 있으며, a 또는 b는 반드시 sqrt(n) 이하의 값이 됩니다.
print(solution([1,2,3,4]))