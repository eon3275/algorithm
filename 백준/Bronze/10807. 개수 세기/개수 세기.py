n = int(input())
list = input().split()
a = input()
cnt=0
for i in range(0, n):
    if list[i]==a:
        cnt+=1
print(cnt)