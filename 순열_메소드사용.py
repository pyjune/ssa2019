from itertools import permutations

A = [4, 7, 8]
N = 3
for p in permutations(range(N)):
    print(A[p[0]], A[p[1]], A[p[2]])
