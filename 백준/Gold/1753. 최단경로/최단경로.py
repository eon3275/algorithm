import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
V, E = map(int, input().split())
K = int(input().strip())
dist = [float('inf')]*(V+1)
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v,w))
queue = [(0, K)]
dist[K] = 0
while queue:
    curr_dist, curr_node = heapq.heappop(queue)
    if dist[curr_node]<curr_dist:
        continue
    for nxt_node, nxt_dist in adj[curr_node]:
        cost = curr_dist + nxt_dist
        if cost<dist[nxt_node]:
            dist[nxt_node] = cost
            heapq.heappush(queue, (cost, nxt_node))
for d in dist[1:]:
    print(f"{'INF' if d==float('inf') else d}\n")
        