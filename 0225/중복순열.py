# 1~m까지 숫자로 k자리수 만들기
def f(n, k, m):
    if(n==k):
        print(p)
    else:
        for i in range (1, m+1):
            p[n] = i
            f(n+1, k, m)

K = 3
M = 5
p = [0]*K
f(0, K, M)
