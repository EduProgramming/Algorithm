import sys
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    stack = [node]

    while stack:
        x = stack.pop()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

def bfs(node):
    visited[node] = True
    queue = [node]

    while queue:
        x = queue.pop(0)
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M = map(int ,input().split())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())
    graph[start] += [end]
    graph[end] += [start]

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        # dfs(i)
        bfs(i)

print(cnt)