N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(len(A)):
    A[i] = A[i] - B
    if A[i] > 0:
        quotien = A[i] // C
        cnt += quotien
        if A[i] % C:
            cnt += 1
cnt += N

print(cnt)