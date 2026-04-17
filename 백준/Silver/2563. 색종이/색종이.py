canvas = [[0 for i in range(100)] for j in range(100)]
N = int(input())
area = 0
for i in range(N):
    x, y = map(int, input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            if canvas[k][j]==0:
               canvas[k][j]=1
            else:
                pass
for i in range(100):
        area+=sum(canvas[i])
print(area)