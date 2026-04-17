s = int(input())
n = int(input())
for i in range(0,n):
    a, b = map(int, input().split())
    s-=a*b
if s==0:
    print("Yes")
else:
    print("No")