A = [1,2,3]
N = 3

for i in range(2**N):
    # i를 비트 단위로 접근
    for j in range(N-1, -1, -1):
        if(i&(1<<j) != 0): # A[j]가 포함되면
            print(A[j], end='')
    print()
for i in range(2**N):
    # i를 비트 단위로 접근
    s = 0
    for j in range(N):
        if(i&(1<<j) != 0): # A[j]가 포함되면
            s += A[j] #  부분집합의 합을 구하는 경우
            print(A[j], end='')
    print(' ', end='')
    print(s)
    print()
