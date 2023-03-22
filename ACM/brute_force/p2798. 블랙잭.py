# N, M = map(int, input().split())
# cards = list(map(int, input().split()))

# maxV = 0
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             sumV = cards[i] + cards[j] + cards[k]
#             if sumV > M:
#                 break
#             if sumV > maxV:
#                 maxV = sumV

# print(maxV)

"""
조합 풀이
: 성능은 반복문 방식이 더 빠름
"""
N, M = map(int, input().split())
cards = list(map(int, input().split()))

pick_num = 3
box = [0] * pick_num
maxV = 0

def combination(n, r):
    global maxV
    if r == 0:
        sumV = 0
        for i in range(pick_num):
            sumV += box[i]
        if sumV > M:
            return
        elif sumV > maxV:
            maxV = sumV
    elif n < r:
        return
    else:
        box[r-1] = cards[n-1]
        combination(n-1, r-1)
        combination(n-1, r)

combination(N, pick_num)
print(maxV)