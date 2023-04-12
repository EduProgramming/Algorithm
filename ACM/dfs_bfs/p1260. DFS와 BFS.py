# [TODO] DFS Stack을 이용한 구현으로 출력 순서 나오게 하기

def dfs(node):
    if visited[node]:
        return
    print(node, end=" ")
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    queue = [node]
    visited[node] = True

    while queue:
        x = queue.pop(0)
        print(x, end=" ")
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())

    graph[start] += [end]
    graph[end] += [start]

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (N+1)
dfs(V)

print()

visited = [False] * (N+1)
bfs(V)