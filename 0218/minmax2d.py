# NxN 배열에서 최대, 최소 찾기
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

# 배열 요소   0<ai<100 인 조건
maxI = 0
maxJ = 0
minI = 0
minJ = 0
# 최대값의 인덱스와 최대값
# 최소값의 인덱스와 최소값
# 같은 값이 있으면 행과 열이 작은쪽을 출력...
for i in range(N):
    for j in range(N):
        if(arr[maxI][maxJ]<arr[i][j]):
            maxI = i
            maxJ = j
        if(arr[minI][minJ]>arr[i][j]):
            minI = i
            minJ = j
print(maxI, maxJ, arr[maxI][maxJ])
print(minI, minJ, arr[minI][minJ])
