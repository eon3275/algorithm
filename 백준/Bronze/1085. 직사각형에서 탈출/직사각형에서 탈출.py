N=list(map(int,input().split()))
for i in range(2):
    N[i+2] = N[i+2]-N[i]
print(min(N))