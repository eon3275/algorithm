import sys
from collections import deque
#input = sys.stdin.readline
C = int(input().strip())
for _ in range(C):
    n = int(input().strip())
    adj = [[False]*(n+1) for _ in range(n+1)]
    prev = list(map(int, input().strip().split()))
    ind = [0]*(n+1)
    for i in range(n):
        for j in range(i+1,n):
            adj[prev[i]][prev[j]]=True
            ind[prev[j]]+=1
    m = int(input().strip())
    for _ in range(m):
        a, b = map(int, input().strip().split())
        if adj[a][b]:
            adj[a][b] = False
            adj[b][a] = True
            ind[b]-=1
            ind[a]+=1
        else:
            adj[b][a] = False
            adj[a][b] = True
            ind[b]+=1
            ind[a]-=1
    queue = deque()
    for i in range(1, n+1):
        if ind[i]==0:
            queue.append(i)
    ans = []
    amb = False
    imp = False
    for _ in range(n):
        if not queue:
            imp = True
            break
        if len(queue)>1:
            amb = True
            break
        curr = queue.popleft()
        ans.append(curr)
        for nxt in range(1, n+1):
            if adj[curr][nxt]:
                ind[nxt]-=1
                if ind[nxt]==0:
                    queue.append(nxt)
    if imp:
        print('IMPOSSIBLE')
    elif amb:
        print('?')
    else:
        print(*ans)