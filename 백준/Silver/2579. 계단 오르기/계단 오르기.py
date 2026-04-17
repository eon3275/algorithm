N = int(input())
stairs = [0]*(N+1)
for i in range(1, N+1):
    stairs[i] = int(input())
dp = [0]*(N+1)
def ans():
    if N==1:
        print(stairs[1])
        return
    elif N==2:
        print(stairs[1]+stairs[2])
        return
    dp[1] = stairs[1]
    dp[2] = stairs[2]+stairs[1]
    dp[3] = max(stairs[3]+stairs[1],stairs[3]+stairs[2])
    for i in range(4, N+1):
        dp[i] = stairs[i] + max(dp[i-2], dp[i-3]+stairs[i-1])
    print(dp[N])
ans()