"""
[방법1] O(N^2)
"""
N = int(input())
P = list(map(int, input().split()))

# 선택정렬 O(N^2)
for i in range(len(P)-1):
    for j in range(i+1, len(P)):
        if P[i] > P[j]:
            # cf) 파이썬은 동시 변경 가능
            # P[i], P[j] = P[j], P[i]
            temp = P[i]
            P[i] = P[j]
            P[j] = temp

result = 0
for i in range(len(P)):
    for j in range(i+1):
        result += P[j]

print(result)

"""
[방법2] O(N^2)
 - 방법1에서 값 합치는 부분을 DP 사용
   해당 부분 로직에서는 O(N)으로 처리함
"""
N = int(input())
P = list(map(int, input().split()))

# 선택정렬 O(N^2)
for i in range(len(P)-1):
    for j in range(i+1, len(P)):
        if P[i] > P[j]:
            # cf) 파이썬은 동시 변경 가능
            # P[i], P[j] = P[j], P[i]
            temp = P[i]
            P[i] = P[j]
            P[j] = temp

sumV = [0] * (len(P) + 1)
for i in range(1, len(P)+1):
    sumV[i] = P[i-1] + sumV[i-1]

result = 0
for i in range(len(sumV)):
    result += sumV[i]

print(result)

"""
[방법3]
  BEST  |  AVERAGE  |  WORST
 O(NlogN) ~ O(NlogN) ~ O(N^2)
"""
# N = int(input())
# P = list(map(int, input().split()))

# DP = [0] * N

# P.sort()

# sumV = 0
# for i in range(len(P)):
#     sumV += P[i]
#     DP[i] = sumV

# result = 0
# for i in range(len(DP)):
#     result += DP[i]

# print(result)