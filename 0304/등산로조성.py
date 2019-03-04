def f(i, j, c, k, n): # i, j 좌표,  n: 크기
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global maxV
    if(maxV < c):
        maxV = c
    for p in range(4): #탐색할 방향
        ni = i + di[p]
        nj = j + dj[p]
        if(ni>=0 and ni<n and nj>=0 and nj<n): #영역을 벗어나지 않고
            if(h[i][j] > h[ni][nj]): #더 낮은 곳으로 이동
                f(ni, nj, c+1, k, n)
            elif(h[i][j] > h[ni][nj]-k):  # 깎아서 이동
                pre = h[ni][nj]
                h[ni][nj] = h[i][j] - 1 # k만큼 깎는게 아니라 이동에 꼭필요한 차이만큼만
                f(ni, nj, c+1, 0, n)
                h[ni][nj] = pre

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    h = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    si = 0
    sj = 0
    for i in range(N):
        for j in range(N):
            if(h[si][sj] < h[i][j]):
                si = i
                sj = j

    for i in range(N):
        for j in range(N):
            if(h[i][j] == h[si][sj]):
                f(i, j, 1, K, N)
    print(f'#{tc} {maxV}')
