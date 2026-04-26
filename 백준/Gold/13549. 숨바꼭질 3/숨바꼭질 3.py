import sys
from collections import deque
N, K = map(int, input().split())
dist = [-1]*100001
queue = deque([N])
dist[N] = 0
while queue:
    curr = queue.popleft()
    if curr==K:
        print(dist[curr])
        break
    for nxt in (curr-1,curr+1,curr*2):
        sec = 0 if nxt==curr*2 else 1
        if 0<=nxt<=100000 and dist[nxt]==-1:
            if nxt==N: continue
            dist[nxt] = dist[curr]+sec
            if sec==0: queue.appendleft(nxt)
            else: queue.append(nxt)