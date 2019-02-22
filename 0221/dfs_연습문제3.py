#7 8
#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(n, v):
    stack = []
    visited = [0]*(v+1) # v번 노드까지 방문표시
    visited[n] = 1
    w = 1
    print(n)
    while(True):
        while(w != 0): # 인접 정점이 있는 경우의 처리     
            w = 0
            for i in range(1, v+1): # n의 인접 정점 찾기
                if(adj[n][i] != 0 and visited[i] == 0):
                    stack.append(n) # 현재 위치 n 저장
                    print(i) # 정점 처리 순서 출력
                    n = i # i로 이동
                    w = 1
                    visited[i] = 1 # 방문 표시
                    break
        if(len(stack)==0): # 되돌아갈 정점이 없으면 중단
            break
        n = stack.pop() # 인접 정점이 없으면 이전 정점으로 이동
        w = 1
V, E = map(int, input().split())
edge = list(map(int, input().split()))

adj = [[0]*(V+1) for i in range(V+1)]
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 방향성이 없는 그래프

dfs(1, V)
