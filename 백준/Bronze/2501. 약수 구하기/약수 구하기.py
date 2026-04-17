a,k=map(int,input().split())
for i in range(1, a+1):
    if a%i==0:
        n=i
        k-=1
    if k==0:
        break
if k!=0:
    n=0
print(n)