import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().strip().split())
adj = [[] for _ in range(N+1)]
ind = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().strip().split())
    adj[A].append(B)
    ind[B]+=1
queue = []
for i in range(1, N+1):
    if ind[i]==0:
        heapq.heappush(queue,i)
ans = []
while queue:
    curr = heapq.heappop(queue)
    ans.append(curr)
    for v in adj[curr]:
        ind[v]-=1
        if ind[v]==0:
            heapq.heappush(queue, v)
print(*ans)
    