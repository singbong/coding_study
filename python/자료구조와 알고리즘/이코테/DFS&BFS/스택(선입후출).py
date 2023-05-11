"""
스택은 접시를 쌓는다는 개념과 비슷한다 가장 먼저 쌓는 접시가 가장
나중에 나오는 것처럼
"""

plate= list()

plate.append(1)
plate.append(2)
plate.append(3)
plate.pop()
print(plate)
#파이썬의 리스트는 기본적으로 선입 선출 append로 쌓고 pop으로 빼는
#스택 구조가 기본적으로 지원이 된다.