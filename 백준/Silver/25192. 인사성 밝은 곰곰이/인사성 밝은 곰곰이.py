import sys
input = sys.stdin.readline
N = int(input())
ans = 0
S = set()
for _ in range(N):
    sysin = input().strip()
    if sysin=='ENTER':
        ans+=len(S)
        S = set()
    else:
        S.add(sysin)
ans+=len(S)
print(ans)