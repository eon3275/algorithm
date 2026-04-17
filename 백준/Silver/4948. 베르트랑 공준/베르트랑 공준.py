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

nums = []
while True:
    num = int(input())
    if num==0: break
    nums.append(num)

for num in nums:
    ans = prime(num*2)
    print(sum(ans[num+1:]))