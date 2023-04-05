"""
DFS 방안을 이용한 
"""

def combi(idx, cnt, visit, n, r):
    if cnt == r:
        for i in range(n):
            if visit[i]:
                print(arr[i], end=" ")
        print()
        return
    
    if idx == n:
        return
    
    visit[idx] = True
    combi(idx+1, cnt+1, visit, n, r)
    visit[idx] = False
    combi(idx+1, cnt, visit, n, r)


N, R = map(int, input().split())

arr = [i for i in range(1, N+1)]
visit = [False] * N

combi(0, 0, visit, N, R)