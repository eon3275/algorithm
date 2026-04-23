import sys
from collections import deque
N, K = map(int, input().strip().split())
dist = [0]*100001
def bfs(N):
    queue = deque([N])
    while queue:
        curr = queue.popleft()
        if curr==K:
            return dist[curr]
        for nxt in (curr+1, curr-1, curr*2):
            if 0<=nxt<=100000 and not dist[nxt]:
                if nxt==N: continue
                dist[nxt] = dist[curr]+1
                queue.append(nxt)
print(bfs(N))