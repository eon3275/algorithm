import sys
input = sys.stdin.readline

def prime(n):
    ans = [True] * (n+1)
    ans[0]=ans[1]=False
    m = int(n**0.5)
    for i in range(2, m+1):
        if ans[i] == True:
            for j in range(i+i, n+1, i):
                ans[j] = False
    return ans

T = int(input())
nums = [int(input()) for _ in range(T)]
ans = prime(max(nums))
for num in nums:
    cnt = 0
    for i in range(2, num//2+1):
        if ans[i] and ans[num-i]:
           cnt+=1
    print(cnt)