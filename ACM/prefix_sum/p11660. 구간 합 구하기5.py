"""
[방안1]
pypy에서만 풀리는 방안
효율적인 방안 찾아볼 것
"""
# N, M = map(int, input().split())
# array = [[0] * N for _ in range(N)]

# S = [[0] * (N+1) for _ in range(N)]

# for i in range(N):
#     num_list = list(map(int, input().split()))
#     for j in range(N):
#         array[i][j] = num_list[j]
#         S[i][j+1] = S[i][j] + array[i][j]

# result = [0] * M
# for i in range(M):
#     start_row, start_col, end_row, end_col = map(int, input().split())
#     sum_value = 0
#     for j in range(start_row-1, end_row):
#         sum_value += S[j][end_col] - S[j][start_col-1]
#     result[i] = sum_value

# for i in range(len(result)):
#     print(result[i])

"""
[방안2]⭐
해당 방안에서는 읽는 부분(input)을 조금 빠르게
처리하는 방안을 사용해야 PASS가 나옴.
"""
N, M = map(int, input().split())
array = [[0] * N for _ in range(N)]

S = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    num_list = list(map(int, input().split()))
    for j in range(N):
        array[i][j] = num_list[j]
        S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + array[i][j]

result = [0] * M
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sum_value = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    result[i] = sum_value

for i in range(len(result)):
    print(result[i])
