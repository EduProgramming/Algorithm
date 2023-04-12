dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
directCnt = 4

def bfs(startRow, startCol):
    q = [startRow, startCol]
    visited[startRow][startCol] = True

    while q:
        row = q.pop(0)
        col = q.pop(0)
        for i in range(directCnt):
            dRow = row + dy[i]
            dCol = col + dx[i]
            if 0 <= dRow < N and 0 <= dCol < M:
                if (not visited[dRow][dCol]) and arr[dRow][dCol] == 1:
                    visited[dRow][dCol] = True
                    q.append(dRow)
                    q.append(dCol)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        col, row = map(int, input().split())
        arr[row][col] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)