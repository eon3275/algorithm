n=int(input())
X=[]
Y=[]
for _ in range(n):
        x,y=map(int,input().split())
        X.append(x)
        Y.append(y)
if n>1:
    x1,y1=min(X), min(Y)
    x2,y2=max(X), max(Y)
    w = x2-x1
    h = y2-y1
    print(w*h)
else:
    print(0)