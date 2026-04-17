N = int(input())
base = [[1,1],[1,0]]
def mul(a, b):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j]%=1000000007
    return res
def solve(n):
    if n<=1:
        return base
    temp = solve(n//2)
    if n%2==0:
        return mul(temp, temp)
    else:
        return mul(mul(temp,temp),base)
ans = solve(N)
print(ans[1][0])