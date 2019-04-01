#7 8
#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def bfs(n, V):
    q = [0]*(V+1) # 큐생성
    front = -1
    rear = -1
    visited = [0] *(V+1)

    rear += 1 #시작노드 인큐
    q[rear] = n
    visited[n] = 1 # 시작노드 방문 표시

    while( front != rear ): # 큐가 비어있지 않으면
        front += 1 # 디큐
        n = q[front]
        print(n, end=' ')  # visit()
        for i in range(1, V+1): # 모든 노드 i 에 대해
            if adj[n][i]!=0 and visited[i]==0: # i가 인접이고 방문안한 노드면
                rear += 1 # i를 인큐하고
                q[rear] = i
                visited[i] = visited[n] + 1 # n에서 방문했음을 표시




V, E = map(int, input().split())
g = list(map(int, input().split()))
adj = [[0]*(V+1) for i in range(V+1)]
for i in range(E):
    n1 = g[i*2]
    n2 = g[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향그래프

bfs(1, V)
