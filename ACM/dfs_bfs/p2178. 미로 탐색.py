# 아래, 오른쪽, 위, 왼쪽
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
directCnt = 4

def bfs(startRow, startCol):
    q = [[startRow, startCol]]
    visited[startRow][startCol] = True

    while q:
        position = q.pop(0)
        row = position[0]
        col = position[1]

        for i in range(directCnt):
            dRow = row + dy[i]
            dCol = col + dx[i]
            if 0 <= dRow < N and 0 <= dCol < M:
                if (not visited[dRow][dCol]) and arr[dRow][dCol] == 1:
                    visited[dRow][dCol] = True
                    arr[dRow][dCol] = arr[row][col] + 1
                    q.append([dRow, dCol])

N, M = map(int, input().split())

arr = [0] * N
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input()))

bfs(0, 0)
print(arr[N-1][M-1])
