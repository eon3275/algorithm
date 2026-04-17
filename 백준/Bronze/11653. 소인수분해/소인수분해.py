N=int(input())
if N>1:
    temp=N
    i=2
    while(temp!=1):
        if temp%i==0:
            print(i)
            temp/=i
        else:
            i+=1