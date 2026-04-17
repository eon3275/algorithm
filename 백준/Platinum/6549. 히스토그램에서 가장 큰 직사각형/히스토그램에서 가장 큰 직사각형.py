import sys
input = sys.stdin.readline
print = sys.stdout.write
def solve(left, right):
    if left==right:
        return hist[left]
    mid = (left+right)//2
    lo = mid
    hi = mid+1
    res = max(solve(left, lo), solve(hi, right))
    h = min(hist[lo], hist[hi])
    res = max(res, h*2)
    while left<lo or hi<right:
        if hi<right and (left==lo or hist[lo-1]<hist[hi+1]):
            hi+=1
            h = min(h, hist[hi])
        else:
            lo-=1
            h = min(h, hist[lo])
        res = max(res, h*(hi-lo+1))
    return res
while True:
    data = list(map(int, input().strip().split()))
    N = data[0]
    if N==0: break
    hist = data[1:]
    print(f'{solve(0,N-1)}\n')