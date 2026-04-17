N=[]
while(1):
    a,b=map(int,input().split())
    if a==b==0:
        break
    N.append((a,b))
for num in N:
    if num[1]%num[0]==0:
        print('factor')
    elif num[0]%num[1]==0:
        print('multiple')
    else:
        print('neither')