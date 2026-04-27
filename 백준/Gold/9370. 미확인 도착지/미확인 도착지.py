import sys
import heapq
input = sys.stdin.readline
def dijk(s, n, adj):
    dist = [float('inf')]*(n+1)
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        curr_weight, curr_node = heapq.heappop(queue)
        if dist[curr_node]<curr_weight: continue
        for d, nxt in adj[curr_node]:
            cost = curr_weight + d
            if cost<dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(queue, (cost, nxt))
    return dist
T = int(input().strip())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        adj[a].append((d, b))
        adj[b].append((d, a))
        if (s, g) == (a, b) or (s, g) == (b, a):
            sg_dist = d
    candidates = [int(input().strip()) for _ in range(t)]
    dist_s = dijk(s, n, adj)
    dist_g = dijk(g, n, adj)
    dist_h = dijk(h, n, adj)
    ans = []
    for can in candidates:
        path_1 = dist_s[g]+dist_g[h]+dist_h[can]
        path_2 = dist_s[h]+dist_h[g]+dist_g[can]
        if dist_s[can] != float('inf') and dist_s[can] == min(path_1, path_2):
            ans.append(can)
    ans.sort()
    print(*ans)