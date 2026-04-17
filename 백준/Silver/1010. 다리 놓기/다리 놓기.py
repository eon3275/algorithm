def fact(N):
    ans = 1
    for i in range(2, N+1):
        ans *= i
    return ans
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fact(M)//fact(N)//fact(M-N))