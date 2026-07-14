from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[-1]*102 for _ in range(102)]
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x:2*x, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1<i<x2 and y1<j<y2:
                    board[i][j] = 0
                elif board[i][j]!=0:
                    board[i][j] = 1
    cx,cy,ix,iy = characterX*2, characterY*2, itemX*2, itemY*2
    visited = set([(cx,cy)])
    q = deque([(cx,cy,0)])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y,step = q.popleft()
        if (x,y)==(ix,iy): return step//2
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<102 and 0<=ny<102:
                if board[nx][ny]==1 and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny,step+1))
    return 0