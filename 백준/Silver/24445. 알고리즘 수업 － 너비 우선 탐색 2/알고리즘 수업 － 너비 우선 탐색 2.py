from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
N,M,R = map(int, input().strip().split())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    v1, v2 = map(int, input().strip().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
for i in range(1, N+1):
    adj[i].sort(reverse=True)
queue = deque([R])
count = 1
visited[R] = 1
while queue:
    curr = queue.popleft()
    for v in adj[curr]:
        if visited[v]==0:
            count+=1
            visited[v]=count
            queue.append(v)
for i in range(1, N+1):
    print(f'{visited[i]}\n')