def dfs(n, v):
    visited[n] = 1 # n번 정점 방문표시
    print(n) # 처리 순서 출력
    for i in range(1, v+1): # n의 인접 정점 찾기
        if(adj[n][i] != 0 and visited[i] == 0):
            dfs(i, v) # n의 인접 i로 이동
            
V, E = map(int, input().split())
edge = list(map(int, input().split()))

adj = [[0]*(V+1) for i in range(V+1)]
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 방향성이 없는 그래프
    visited = [0]*(V+1) # v번 노드까지 방문표시
dfs(1, V)
