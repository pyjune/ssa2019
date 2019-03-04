
def f(i, j, n):
    global cnt
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if (maze[i][j] == 3) : # 목적지에 도착한 경우
        cnt += 1
        return
    else:
        maze[i][j] = 1 # 방문한 칸으로 미로에 직접 표시
        for k in range(4): # 주변 칸의 좌표 계산
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<n): # 미로를 벗어나지 않으면
                if(maze[ni][nj] != 1): # ni, nj 칸이 벽이 아니면 이동
                    f(ni, nj, n)
        maze[i][j] = 0 # 이전의 갈림길에서 다른 경로로 진입하는 것은 허용
        return # 가능한 모든 방향에서 목적지를 찾지 못하면

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for i in range(N)] #문자열로 저장하는 경우 방문표시 배열 필요
    startI = -1
    startJ = -1
    for i in range(N):
        for j in range(N):
            if(maze[i][j]==2):
                startI = i
                startJ = j
                break
        if(startI!=-1):
            break
    cnt = 0
    f(startI, startJ, N)
    print(f'#{tc} {cnt}')

