h, m = map(int, input().split())
t = int(input())
h +=int(t/60)
m += int(t%60)
if m>=60:
    m-=60
    h+=1
if h>=24:
    h-=24
print(h, m)