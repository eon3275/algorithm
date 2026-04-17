import sys
#input = sys.stdin.readline
N,M,K = map(int, input().split())
matrix = [input().strip() for _ in range(N)]
S = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        color = 'W' if (i + j) % 2 == 0 else 'B'
        err = 1 if matrix[i][j] != color else 0
        S[i+1][j+1] = S[i][j+1] + S[i+1][j] - S[i][j] + err
def ans():
    res = K*K
    for i in range(N-K+1):
        for j in range(M-K+1):
            cnt = S[i+K][j+K]-S[i][j+K]-S[i+K][j]+S[i][j]
            res = min(res, cnt, K*K-cnt)
    return res
print(ans())