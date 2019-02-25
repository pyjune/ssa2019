def f(n, k, m, s, rs): # s : n-1까지 포함된 원소의 합
    global cnt
    global cnt2
    cnt2 += 1
    if (s==m):
        cnt += 1
    elif (n==k): # 한개의 부분집합 완성
        return
    elif (m<s):
        return
    elif (s+rs<m):
        return
    else:
        b[n] = 0
        f(n+1, k, m, s, rs-a[n]) # a[n]이 포함되지 않는 경우
        b[n] = 1
        f(n+1, k, m, s+a[n], rs-a[n]) # a[n]이 포함되는 경우

K = 10
M = 27 # 부분집합의 합
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #  주어진 집합
b = [0]*K # 원소의 포함여부를 나타내는 배열
cnt = 0
cnt2 = 0
f(0, K, M, 0, sum(a))
print(cnt, cnt2)
