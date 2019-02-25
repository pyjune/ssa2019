def f(n, k):
    if (n==k):
        #print(b)
        for i in range(k):
            if(b[i]==1):
                print(a[i], end=' ')
        print()
        return
    else:
        b[n] = 0
        f(n+1, k)
        b[n] = 1
        f(n+1, k)

K = 3
a = [10, 20, 30] #  주어진 집합
b = [0]*K # 원소의 포함여부를 나타내는 배열
f(0, K)
