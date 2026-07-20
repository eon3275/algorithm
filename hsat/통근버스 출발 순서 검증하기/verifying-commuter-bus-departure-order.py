N = int(input())
a = list(map(int, input().split()))

# Please write your code here.
answer = 0
for i in range(N-2):
    cnt = 0
    for k in range(i+1,N):
        if a[k]<a[i]:
            cnt+=1
    for j in range(i+1,N):
        if a[j]<a[i]:
            cnt-=1
        else:
            answer+=cnt
print(answer)