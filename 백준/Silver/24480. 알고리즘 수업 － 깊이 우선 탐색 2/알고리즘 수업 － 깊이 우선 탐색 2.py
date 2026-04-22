import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M, R = map(int, input().strip().split())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    i, o = map(int, input().strip().split())
    adj[i].append(o)
    adj[o].append(i)
for i in range(1, N+1):
    adj[i].sort()
count=1
stack=[R]
while stack:
    curr = stack.pop()
    if visited[curr]!=0:
        continue
    visited[curr] = count
    count+=1
    for v in adj[curr]:
        if visited[v]==0:
            stack.append(v)
for i in range(1, N+1):
    print(f'{visited[i]}\n')
