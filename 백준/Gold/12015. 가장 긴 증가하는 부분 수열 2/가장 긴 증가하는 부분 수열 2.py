N = int(input())
A = list(map(int, input().split()))
lis = [A[0]]

def find(target):
    low = 0
    high = len(lis)
    while low<high:
        mid = (low+high)//2
        if lis[mid]>=target:
            high = mid
        else:
            low = mid+1
    return low
for i in range(1, N):
    current = A[i]
    if current>lis[-1]:
        lis.append(current)
    else:
        idx = find(current)
        lis[idx] = current
print(len(lis))