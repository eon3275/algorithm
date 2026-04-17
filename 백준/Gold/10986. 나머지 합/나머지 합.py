N, M = map(int, input().split())
nums = list(map(int, input().split()))
mod = [0]*M
curr = 0
for n in nums:
    curr = (curr+n)%M
    mod[curr] += 1
ans = mod[0]
for c in mod:
    if c>=2:
        ans+=c*(c-1)//2
print(ans)