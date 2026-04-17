def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

T = int(input())
ans = []
for _ in range(T):
    a, b = map(int, input().split())
    ans.append(a//gcd(a, b)*b)
for o in ans:
    print(o)