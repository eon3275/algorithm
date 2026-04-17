N, M = map(int, input().split())
trees = list(map(int, input().split()))

def solve():
    start, end = 1, max(trees)
    while start<=end:
        mid = (start+end)//2
        con = 0
        for t in trees:
            con+=(t-mid) if t>mid else 0
        if con>=M: #higher
            start = mid+1
        else: #lower
            end = mid-1
    return end
print(solve())