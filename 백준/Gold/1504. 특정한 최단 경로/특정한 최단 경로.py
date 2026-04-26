import heapq
import sys
input = sys.stdin.readline
N, E = map(int, input().split())
INF = 10e9
adj = [[] for _ in range(N+1)]
for _ in range(E):
    v1, v2, d = map(int, input().split())
    adj[v1].append((d, v2))
    adj[v2].append((d, v1))
def dijk(start):
    dist = [INF]*(N+1)
    dist[start]=0
    queue = [(0, start)]
    while queue:
        d, curr = heapq.heappop(queue)
        if dist[curr]<d: continue
        for w, nxt in adj[curr]:
            cost = d+w
            if cost<dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(queue, (cost, nxt))
    return dist
v1, v2 = map(int, input().split())
start_1 = dijk(1)
start_v1 = dijk(v1)
start_v2 = dijk(v2)
path_1 = start_1[v1]+start_v1[v2]+start_v2[N]
path_2 = start_1[v2]+start_v2[v1]+start_v1[N]
answer = min(path_1, path_2)
if answer>=INF:
    print(-1)
else:
    print(answer)