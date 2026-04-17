import sys
N = int(sys.stdin.readline()) 
nums = list((map(int, sys.stdin.readline().split())))
s = sorted(list(set(nums)))
dicts = {value: i for i, value in enumerate(s)}
for n in nums:
    print(dicts[n], end=' ')