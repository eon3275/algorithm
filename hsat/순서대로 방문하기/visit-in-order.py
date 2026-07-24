n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append((x - 1, y - 1))

# Please write your code here.
dx, dy = [-1,1,0,0], [0,0,-1,1]
sx, sy = points[0]
grid[sx][sy] = 1
def backtracking(step, x, y):
    if step==m: return 1
    total = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
            chkpoint = 1 if (nx,ny)==points[step] else 0
            grid[nx][ny] = 1
            total+=backtracking(step+chkpoint,nx,ny)
            grid[nx][ny] = 0
    return total
print(backtracking(1,sx,sy))
        