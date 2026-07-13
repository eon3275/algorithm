from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dydx = [[1,0],[-1,0],[0,1],[0,-1]]
    q = deque([(0,0)])
    while q:
        cy, cx = q.popleft()
        for dy, dx in dydx:
            ny, nx = cy+dy, cx+dx
            if 0<=ny<n and 0<=nx<m and maps[ny][nx]==1:
                maps[ny][nx]=maps[cy][cx]+1
                q.append((ny,nx))
    return maps[n-1][m-1] if maps[n-1][m-1]!=1 else -1
        