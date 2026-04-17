num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N,B=input().split()
B=int(B)
N=N[::-1]
result=0
for i,n in enumerate(N):
    result+=num.index(n)*(B**i)
print(result)
