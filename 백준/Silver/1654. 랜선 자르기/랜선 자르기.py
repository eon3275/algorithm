K, N = map(int, input().split())
data = [int(input()) for _ in range(K)]

def solve():
    start, end = 1, max(data)
    while start<=end:
        mid = (start+end)//2
        lines = 0
        for d in data:
            lines+=d//mid
        if lines>=N:
            start = mid+1
        else:
            end = mid-1
    return end
print(solve())
    