"""
링크드리스트를 이용한 로또 번호 추첨기 만들기
"""
import random


##전역 변수##
pre, head, current= None, None, None
memory= []


##노드 출력 함수##

def printNodes(start):
    current= start
    if current == None:
        return
    
    print(current.data, end=' ')
    while current.link != None:
        current= current.link
        print(current.data, end=' ')
    print()

def orderNode(insert_data):

    return

##메인 함수##

if __name__ == '__main__':

    
