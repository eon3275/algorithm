import sys
from collections import deque
T = int(input().strip())
dx = [-2,-2,2,2,-1,-1,1,1]
dy = [-1,1,-1,1,-2,2,-2,2]
def bfs(I,sx,sy,ex,ey):
    board = [[0]*I for _ in range(I)]
    queue = deque([(sx,sy)])
    while queue:
        cx,cy = queue.popleft()
        if cx == ex and cy == ey:
            break
        for i in range(8):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<I and 0<=ny<I:
                if not (nx==sx and ny==sy) and board[nx][ny]==0:
                    board[nx][ny] = board[cx][cy]+1
                    queue.append((nx,ny))
    print(board[ex][ey])

for _ in range(T):
    I = int(input().strip())
    sx,sy = map(int, input().strip().split())
    ex,ey = map(int, input().strip().split())
    bfs(I,sx,sy,ex,ey)