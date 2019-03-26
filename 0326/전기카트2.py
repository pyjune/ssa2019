import sys

def find(n, k, s):                     # n은 순열의 인덱스, k는 이전 방문위치, s는 현재까지의 소모량
    global minV
    if n == N:                      # 순열이 완성된 경우
        s += e[k][0]                # 사무실까지의 거리 추가
        if minV>s:                  # 기존의 최소값보다 작으면
            minV = s
        return
    elif minV <= s:                 # 순열이 완성되지 않았지만 합이 최소값보다 큰 경우
        return
    else:
        for i in range(1, N):          # 순열의 n번 인덱스에 들어갈 숫자 선택
            if u[i] == 0:
                u[i] = 1
                find(n+1, i, s+e[k][i])
                u[i] = 0
        return

sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int,input().split())) for x in range (N)]
    u = [0 for i in range(N+1)]                   # 사용한 숫자 표시
    p = [0 for i in range(N+1)]                   # 순열저장
    minV = 10000
    u[0] = 1                            # 0번은 사무실이므로 고정
    find(1, 0, 0)
    print('#{} {}'.format(tc, minV))
