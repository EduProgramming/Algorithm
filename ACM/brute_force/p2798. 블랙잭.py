N, M = map(int, input().split())
cards = list(map(int, input().split()))

maxV = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sumV = cards[i] + cards[j] + cards[k]
            if sumV > M:
                break
            if sumV > maxV:
                maxV = sumV

print(maxV)