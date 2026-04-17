while(1):
    n=int(input())
    if n==-1:
        break
    N=[]
    for i in range(1, n):
        if n%i==0:
            N.append(i)
    if n==sum(N):
        print(n, ' = ', ' + '.join(map(str,N)), sep='')
    else:
        print('%d is NOT perfect.'%n)