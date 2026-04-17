N, M = map(int, input().split())
temp = [0]*N
for _ in range(0, M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        temp[n] = k
for t in range(0, N):
    print(temp[t], end=" ")