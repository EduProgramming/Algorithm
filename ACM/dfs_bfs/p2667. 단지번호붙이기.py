dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
directCnt = 4

def bfs(startRow, startCol):
    q = [startRow, startCol]
    visited[startRow][startCol] = True
    v = 1

    while q:
        row = q.pop(0)
        col = q.pop(0)
        for i in range(directCnt):
            dRow = row + dy[i]
            dCol = col + dx[i]
            if 0 <= dRow < N and 0 <= dCol < N:
                if not visited[dRow][dCol] and arr[dRow][dCol] == 1:
                    visited[dRow][dCol] = True
                    q.append(dRow)
                    q.append(dCol)
                    v += 1
    return v

N = int(input())
arr = [0] * N

visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input()))

cnt = 0
value_list = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            cnt += 1
            value = bfs(i, j)
            value_list.append(value)

value_list.sort()

print(cnt)
for value in value_list:
    print(value)