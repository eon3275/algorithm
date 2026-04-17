N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
lines.sort()
B = [x[1] for x in lines]
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if B[j]<B[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))
            