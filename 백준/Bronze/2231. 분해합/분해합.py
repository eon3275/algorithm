def calculate(N):
    num = N
    ans = 0
    while num!=0:
        ans+=num%10
        num=num//10
    return ans+N

N = int(input())
ans = N
for i in range(1, N+1): #1부터 N까지
    temp = calculate(i)
    if (N==temp) and (ans > i):
        ans = i
if ans == N:
    ans = 0
print(ans)