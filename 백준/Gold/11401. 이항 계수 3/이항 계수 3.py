N, K = map(int, input().split())
P = 1000000007
def power(a,b):
    return pow(a,b,P)
fact = [1]*(1+N)
for i in range(1, N+1):
    fact[i] = (fact[i-1]*i)%P
nu = fact[N]
de = (fact[N-K]*fact[K])%P
ans = (nu*power(de, P-2))%P
print(ans)