n = int(input())
N = list(map(int,input().split()))
count=0
for num in N:
    cnt = 0
    if num>1:
        for i in range(2, num):
            if num%i==0:
                cnt+=1
        if cnt == 0:
            count +=1
print(count)