nums = list(map(int, input().split()))
c = max(nums)
r = sum(nums)-c
if c>=r:
    print(2*r-1)
else:
    print(r+c)
