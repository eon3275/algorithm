M = int(input())
N = int(input())
List=[]
for i in range(M, N+1):
    cnt = 0
    if i>1:
        for j in range(2, i):
            if i%j==0:
                cnt+=1
                break
        if cnt == 0:
            List.append(i)
if len(List)<1:
    print(-1)
else:
    print(sum(List))
    print(min(List))