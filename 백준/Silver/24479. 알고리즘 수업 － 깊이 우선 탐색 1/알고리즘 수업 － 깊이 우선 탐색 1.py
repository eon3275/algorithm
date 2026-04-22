import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**6)
N, M, R = map(int, input().strip().split())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    i, o = map(int, input().strip().split())
    adj[i].append(o)
    adj[o].append(i)
for i in range(1, N+1):
    adj[i].sort()

count = 1
def dfs(R):
    global count
    visited[R] = count
    for v in adj[R]:
        if visited[v]==0:
            count+=1
            dfs(v)
dfs(R)
for i in range(1, N+1):
    print(f'{visited[i]}\n')
