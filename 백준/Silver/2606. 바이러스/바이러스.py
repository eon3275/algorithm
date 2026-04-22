from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input().strip())
M = int(input().strip())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().strip().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
visited = [False]*(N+1)
queue = deque([1])
visited[1] = True
count = 0
while queue:
    curr = queue.popleft()
    for v in adj[curr]:
        if not visited[v]:
            count+=1
            visited[v] = True
            queue.append(v)
print(f'{count}\n')