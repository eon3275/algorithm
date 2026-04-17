import sys
input = sys.stdin.readline
N = int(input())
nums = sorted(list(map(int, input().strip().split())))
print(nums[0]*nums[-1])