x=[]
y=[]
for i in range(3):
    X,Y = map(int,input().split())
    x.append(X)
    y.append(Y)

x1=x.count(max(x))
x2=x.count(min(x))
y1=y.count(max(y))
y2=y.count(min(y))
if x1>x2:
    rx=min(x)
else:
    rx=max(x)
if y1>y2:
    ry=min(y)
else:
    ry=max(y)
print(rx, ry)