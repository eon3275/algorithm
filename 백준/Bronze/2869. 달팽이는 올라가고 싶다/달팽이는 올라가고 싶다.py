A,B,V = map(int,input().split())
days = (V-A)/(A-B)+1
if days%1!=0:
    days=int(days)+1
else:
    days=int(days)
print(days)