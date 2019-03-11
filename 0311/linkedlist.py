class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n

def addFirst(data):
    global Head
    Head = Node(data, Head)

def search(data): # data가 들어있는 Node의 주소를 리턴
    global Head
    p = Head
    while(p!=None and p.item!=data): #노드는 존재하지만 찾는 값을 갖고 있지 않으면
        p = p.link  # 다음 노드로 이동
    return p

def add(data1, data2): # data1 뒤에 data2 노드 추가
    p = search(data1)
    p.link = Node(data2, p.link)

#Head -> 30|link -> 20|link -> 10|link
Head = None
addFirst(10)
addFirst(20)
addFirst(30)
add(20, 15) # 20 뒤에 15 노드를 추가

p = Head
while(p!=None): # 30, 20, 15, 10을 순서대로 출력
    print(p.item)
    p = p.link

print(Head.link)
print(search(20))

print(Head.item)
print(Head.link.item)
print(Head.link.link.item)
print(Head.link.link.link)

