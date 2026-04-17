import sys
print = sys.stdout.write
N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))
def solve(left, right, target):
    if left>right:
        return 0
    mid = (left+right)//2
    if nums[mid]==target:
        return 1
    elif nums[mid]<target:
        return solve(mid+1, right , target)
    else:
        return solve(left, mid-1, target)
for t in targets:
    print(f'{solve(0, N-1, t)}\n')