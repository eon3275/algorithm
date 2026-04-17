import sys
N, M = map(int, sys.stdin.readline().split())
n = set()
m = []
for _ in range(N):
    n.add(sys.stdin.readline().rstrip())
for _ in range(M):
    m.append(sys.stdin.readline().rstrip())
ans = 0
for word in m:
    if word in n:
        ans+=1
print(ans)