import sys
input = sys.stdin.readline
N, C = map(int, input().strip().split())
house = sorted([int(input().strip()) for _ in range(N)])

def solve():
    start = 1
    end = house[-1]-house[0]
    while start<=end:
        count=1
        last = house[0]
        mid = (start+end)//2
        for h in house[1:]:
            if h-last>=mid:
                count+=1
                last = h
        if count>=C:
            start = mid+1
        else:
            end = mid-1
    return end
print(solve())