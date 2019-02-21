# 방문안한 인접 정점을 push하는 방식의 코드입니다.
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(n, v):
    stack = []
    visited = [0]*(v+1) # v번 노드까지 방문표시
    visited[n] = 1
    stack.append(n)
    while(len(stack) != 0): # 스택이 비어있지 않으면
        n = stack.pop() # 인접 노드 중 하나를 꺼내서 방문
        print(n, end=' ')
        #for i in range(1, v+1):
        for i in range(v, 0, -1):
            if(adj[n][i] != 0 and visited[i] == 0): # n 과 i가 인접이고 방문하지 않은 노드면
                stack.append(i) # n에 인접한 모든 노드를 push
                visited[i] = 1


V, E = map(int, input().split())
edge = list(map(int, input().split()))

adj = [[0]*(V+1) for i in range(V+1)]
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 방향성이 없는 그래프

dfs(1, V)
