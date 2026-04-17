import sys
N = int(sys.stdin.readline().strip())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))
nums.sort()
for i in range(N):
    print(nums[i])