N = int(input())
nums = [0]*N
for i in range(N):
    nums[i] = int(input())
dp = [0]*N
def ans():
    if N==1:
        print(nums[0])
        return
    elif N==2:
        print(nums[0]+nums[1])
        return
    dp[0] = nums[0]
    dp[1] = dp[0]+nums[1]
    dp[2] = max(nums[0]+nums[1], nums[0]+nums[2], nums[1]+nums[2])
    for i in range(3, N):
        dp[i] = max(dp[i-1], nums[i]+dp[i-2], dp[i-3]+nums[i-1]+nums[i])
    print(dp[N-1])
ans()