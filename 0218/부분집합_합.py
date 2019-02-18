# 부분집합이 합이 0인 경우가 있으면 1, 없으면 0을 출력하는 프로그램
# 공집합 제외

def find(arr, N):
    for i in range(1, 2**N): # 1 ~ 2**N-1  생성 (0인 경우 공집합이고 합이 0이 됨)
        s = 0
        for j in range(N): # 0~N번 비트 검사 (1개의 부분 집합 검사)
            if(i & (1 << j) != 0): #  arr[j] 포함여부 검사
                s += arr[j]
        if(s == 0):
            return 1
    return 0

A = [-7, -3, -2, -5, -8]
N = len(A)

print(find(A, N))
