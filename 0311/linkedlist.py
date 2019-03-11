class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n

def addFirst(data):
    global Head
    Head = Node(data, Head)

def addLast(data):
    global Head
    p = Head
    while(p.link!=None):
        p = p.link
    p.link = Node(data)

def search(data): # data가 들어있는 Node의 주소를 리턴
    global Head
    p = Head
    while(p!=None and p.item!=data): #노드는 존재하지만 찾는 값을 갖고 있지 않으면
        p = p.link  # 다음 노드로 이동
    return p

def add(data1, data2): # data1 뒤에 data2 노드 추가
    p = search(data1)
    p.link = Node(data2, p.link)

def delete(data):
    global Head
    if(Head==None):
        return
    p1 = None
    p2 = Head
    while(p2!=None and p2.item!=data):
        p1 = p2
        p2 = p2.link
    if(p2==None): # data가 없는 경우
        return
    elif(p1==None): # data가 맨 앞 노드에 있는 경우
        Head = p2.link
    else:
        p1.link = p2.link # data가 맨 앞 노드가 아닌 경우




#Head -> 30|link -> 20|link -> 10|link
Head = None
addFirst(10)
addFirst(20)
addFirst(30)
add(20, 15) # 20 뒤에 15 노드를 추가
delete(20)
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

