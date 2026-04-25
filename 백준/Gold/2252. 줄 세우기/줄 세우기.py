import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().strip().split())
adj = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    v1, v2 = map(int, input().strip().split())
    adj[v1].append(v2)
    indegree[v2]+=1
queue = deque()
for i in range(1, N+1):
    if indegree[i]==0:
        queue.append(i)
ans = []
while queue:
    curr = queue.popleft()
    ans.append(curr)
    for v in adj[curr]:
        indegree[v]-=1
        if indegree[v]==0:
            queue.append(v)
print(*ans)