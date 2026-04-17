N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
ans = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            ans[i][j] += A[i][k]*B[k][j]
for i in range(N):
    print(' '.join(map(str, ans[i])))