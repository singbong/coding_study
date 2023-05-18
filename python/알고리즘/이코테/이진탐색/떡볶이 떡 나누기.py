"""
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다. 오늘은 떡볶이 떡을 만드는 날입
니다. 동빈이네 떡볶이 떡은 재밌게도 떡의 길이가 일정하지 않습니다. 대신에 한 봉지 안에
들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.

절단기에 높이를 지정하면 줄지어진 떡을 한번에 절단합니다. 높이가 H보다 긴 떡은 H위의
부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다.

예를 들어 높이가 19,14,10,17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤
떡의 높이는 15,14,10,15cm가 될 것입니다. 잘린 떡의 길이는 차례대로 4,0,0,2cm입니다.
손님은 6cm만큼의 길이를 가져갑니다.

손님이 왔을때 요청한 길이가 총 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는
높이의 최댓값을 구하는 프로그램을 작성하세요.

1<= N <= 1,000,000 , 1<= M <= 2,000,000,000

이렇게 큰값을 만나면 이진탐색을 떠올려야하고 
잘린떡이 내가 값을 얼마를 주냐에 따라 커지거나 작아지거나 yes or no 형태이기때문에 이진탐색을 사용할 수 있다.
"""
n, m = map(int, input().split())
array= list(map(int, input().split()))

start= 0
end= max(array)+1

result= 0
def finder(array, start, end):
    while start <= end:
        mid= (start+end)//2
        total= 0
        for i in array:
            if mid < i:
                total += i-mid
        
        if total <= m:
            result= mid
            end= mid-1
        else:
            start= mid+1
    else:
        return result
    
print(finder(array, start, end))

  

 