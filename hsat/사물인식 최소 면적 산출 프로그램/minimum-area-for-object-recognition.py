N, K = map(int, input().split())
points = [[] for _ in range(K + 1)]

for _ in range(N):
    x, y, k = map(int, input().split())
    points[k].append((x, y))
# Please write your code here.
min_area = 4e6
def dfs(k,min_x,max_x,min_y,max_y):
    global min_area
    if min_area==0: return
    area = (max_x-min_x)*(max_y-min_y)
    if k>1:
        if area>=min_area: return
    if k>K:
        min_area = area
        return
    for x,y in points[k]:
        dfs(k+1,min(min_x,x),max(max_x,x),min(min_y,y),max(max_y,y))        
dfs(1,1000,-1000,1000,-1000)
print(min_area)