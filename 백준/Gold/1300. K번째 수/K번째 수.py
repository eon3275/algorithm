N = int(input())
K = int(input())
low = 1
high = K
ans = 0
while low<=high:
    mid = (low+high)//2
    count = 0
    for i in range(1,N+1):
        count+=min(N, mid//i)
    if count>=K:
        ans = mid
        high = mid-1
    else:
        low = mid+1
print(ans)