import sys
import itertools

def find():
    minV = 100000                       # 최소값 초기화
    lst = [i for i in range(1, N)]                      # 구역은 1에서 N-1번
    p = list(itertools.permutations(lst))           # 순열 생성 후 리스트에 저장
    for i in range(len(p)):                             # 순열 개수 만큼 반복
        s = e[0][p[i][0]]                                   # 사무실-첫 구역간 소비량
        for j in range(1, N-1):                                  # 구역간 소비량, N-1구역은 N-2인덱스에 들어있음
            s += e[p[i][j-1]][p[i][j]]
        s +=e[p[i][N-2]][0]                                # 마지막 구역-사무실
        if s<minV:
            minV = s
    return minV

    
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = int(input())                   
    e = [list(map(int,input().split())) for i in range(N)]      # 사무실 0번, 마지막 구역 N-1번
    print('#{} {}'.format(tc, find()))
