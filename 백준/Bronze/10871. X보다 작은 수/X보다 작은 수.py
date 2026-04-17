N, X = map(int, input().split())
numList = list(map(int, input().split()))
for i in range(0, N):
    if numList[i]<X:
        print(numList[i], end=" ")