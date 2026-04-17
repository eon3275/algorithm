import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
nums = [0]+list(map(int, input().strip().split()))
for i in range(1, N+1):
    nums[i] += nums[i-1]
for _ in range(M):
    i1, i2 = map(int, input().strip().split())
    print(nums[i2]-nums[i1-1])
