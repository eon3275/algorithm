arr = [int(input())%42 for i in range(0,10)]
cnt = 0
for i in range(0, 10):
    if arr[i] < 0:
        continue
    for j in range(i, 10):
        if i == j:
            continue
        elif arr[i]==arr[j]:
            arr[j]=-1
for i in range(0, 10):
    if arr[i]>=0:
        cnt+=1
print(cnt)