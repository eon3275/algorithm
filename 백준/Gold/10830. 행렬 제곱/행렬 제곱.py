N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
def mul(a,b):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j] %= 1000
    return res
def solve(a,b):
    if b==1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    temp = solve(a, b//2)
    if b%2==0:
        return mul(temp, temp)
    else:
        return mul(mul(temp,temp),a)
ans = solve(A,B)
for r in ans:
    print(*r)