N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, 1 << N):
    sumV = 0
    for j in range(N):
        if i & 1 << j:
            sumV += arr[j]
    if sumV == S:
        cnt += 1

print(cnt)