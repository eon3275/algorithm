def prime(n):
    ans = [True] * (n+1)
    ans[0]=ans[1]=False
    m = int(n**0.5)
    for i in range(2, m+1):
        if ans[i] == True:
            for j in range(i+i, n+1, i):
                ans[j] = False
    return ans

M, N = map(int, input().split())
ans = prime(N)
for i in range(M,N+1):
    if ans[i]: print(i)