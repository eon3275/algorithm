N, B = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
l, r = min(a), 2*10**9
while l<=r:
    budget = B
    mid = (l+r)//2
    for i in range(N):
        if mid>a[i]: budget-=(mid-a[i])**2
        if budget<0:
            r = mid-1
            break
    if budget>=0:
        l = mid+1
print(r)