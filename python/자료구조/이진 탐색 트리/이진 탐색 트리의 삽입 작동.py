## 함수 선언 부분##
class TreeNode():
    def __init__(self):
        self.left= None
        self.right= None
        self.data= None

##전연 변수 선언 부분##
memory= []
root= None
array= ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스','잇지','여자친구']

##메인 코드 부분##
node= TreeNode()
node.data= array[0]
root= node
memory.append(node)

for name in array[1:]:

    node= TreeNode()
    node.data = name

    current= root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current= current.left
        else:
            if current.right == None:
                current.right= node
                break
            current= current.right
    memory.append(node)

findName= ''

while 1:
    findName= input('찾을 그룹 이름(x=프로그램종료)--> ')
    current= root
    if findName == 'x' or findName== 'X':
        break
        
    while True:
        if findName == current.data:
            print(findName, '을 찾음')
            break
        elif findName < current.data:
            if current.left == None:
                print(findName, '이 트리에 없음')
                break
            current= current.left
        else:
            if current.right == None:
                print(findName, '이 트리에 없음')
                break
            current= current.right
