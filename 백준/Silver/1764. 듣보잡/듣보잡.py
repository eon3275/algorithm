import sys
N, M = map(int,sys.stdin.readline().rstrip().split())
n, m = set(), set()
for _ in range(N):
    n.add(sys.stdin.readline().rstrip())
for _ in range(M):
    m.add(sys.stdin.readline().rstrip())
ans = sorted(n & m)
sys.stdout.write(f'{len(ans)}\n')
for name in ans:
    sys.stdout.write(name+'\n')