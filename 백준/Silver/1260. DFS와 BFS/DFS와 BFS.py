import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(start):
    visited = [False]*(N+1)
    stack = [start]
    ans = []
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            ans.append(curr)
            visited[curr] = True
            for v in adj[curr][::-1]:
                if not visited[v]:
                    stack.append(v)
    return ans
def bfs(start):
    ans=[]
    visited = [False]*(N+1)
    queue = deque([start])
    visited[start]=True
    while queue:
        curr = queue.popleft()
        ans.append(curr)
        for v in adj[curr]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return ans
N, M, V = map(int, input().strip().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().strip().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
for i in range(1, N+1):
    adj[i].sort()
    
print(*dfs(V))
print(*bfs(V))