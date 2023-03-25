"""
얕은 복사로 인하여 문제가 생겼던게 껄끄러웠던 문제
"""

N = int(input())
arr = [i for i in range(1, N+1)]

M = 1
for i in range(2, N+1):
    M *= i
result = [[0] * N for _ in range(M)]
idx = 0

def perm(n, k):
    global idx
    if n == k:
        for i in range(N):
            result[idx][i] = arr[i]
        idx += 1
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

perm(N, 0)
result.sort()

for i in range(M):
    for j in range(N):
        print(result[i][j], end=" ")
    print()