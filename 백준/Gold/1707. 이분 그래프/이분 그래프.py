import sys
from collections import deque
input = sys.stdin.readline
K = int(input().strip())
def bfs(start, adj, visited):
    visited[start]=1
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        for v in adj[curr]:
            if visited[v]==0:
                visited[v] = -1*visited[curr]
                queue.append(v)
            elif visited[v]==visited[curr]:
                return False
    return True
def solve(V,adj, visited):
    for i in range(1,V+1):
        if visited[i]==0:
            if not bfs(i, adj, visited):
                return False
    return True
for _ in range(K):
    V, E = map(int, input().strip().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().strip().split())
        adj[u].append(v)
        adj[v].append(u)
    visited = [0]*(V+1)
    print('YES' if solve(V,adj,visited) else 'NO')