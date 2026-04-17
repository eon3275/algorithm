N, K = map(int, input().split())
nums = [0]+list(map(int, input().split()))
for i in range(1, N+1):
    nums[i] += nums[i-1]
max_val = -float('inf')
for i in range(K,N+1):
    sum_val = nums[i]-nums[i-K]
    if max_val < sum_val:
        max_val = sum_val
print(max_val)