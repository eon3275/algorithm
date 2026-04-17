N = int(input())
tr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(i+1):
        if j==0:
            tr[i][j] += tr[i-1][j]
        elif j==i:
            tr[i][j] += tr[i-1][j-1]
        else:
            tr[i][j] += max(tr[i-1][j], tr[i-1][j-1])
print(max(tr[N-1]))
