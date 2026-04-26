import sys
import heapq
N, K = map(int, input().split())
dist = [float('inf')]*100001
queue = [(0, N)]
dist[N] = 0
while queue:
    d, curr = heapq.heappop(queue)
    if curr==K:
        print(d)
        break
    if dist[curr]<d: continue
    for nxt, t in [(curr*2, 0), (curr+1, 1), (curr-1, 1)]:
        if 0<=nxt<=100000:
            cost = d + t
            if cost<dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(queue, (cost, nxt))