def bfs(node):
    q = [node]

    while q:
        x = q.pop(0)
        if tree[x] != -1:
            graph[tree[x]].remove(x)

        for i in graph[x]:
            q.append(i)
        graph[x].append(-1)

N = int(input())
tree = list(map(int, input().split()))
REMOVE_NODE = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    if tree[i] == -1:
        continue
    graph[tree[i]].append(i)

bfs(REMOVE_NODE)

cnt = 0
for i in range(len(graph)):
    if not graph[i]:
        cnt += 1

print(cnt)