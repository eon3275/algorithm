import sys
input = sys.stdin.readline
print = sys.stdout.write
INF = float('inf')
def bf(start):
    dist[start] = 0
    for i in range(N):
        for a, b, c in edges:
            if dist[a]!=INF and dist[b] > dist[a]+c:
                dist[b] = dist[a]+c
                if i==N-1:
                    return True
    return False
N, M = map(int, input().split())
dist = [INF]*(N+1)
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A,B,C))
neg_cycle = bf(1)
if neg_cycle:
    print(f'{-1}\n')
else:
    for i in range(2, N+1):
        if dist[i]==INF:
            print(f'{-1}\n')
        else:
            print(f'{dist[i]}\n')