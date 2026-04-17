import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())
coins = [int(input().strip()) for _ in range(N)]
ans = 0
idx = N-1
while K!=0:
    if coins[idx]<=K:
        quo = K//coins[idx]
        ans += quo
        K -= quo*coins[idx]
    idx-=1
print(ans)