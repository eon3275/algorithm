import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    queue = deque([(0,0)])
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if maze[ny][nx]==1 and not (nx==0 and ny==0):
                    maze[ny][nx] = maze[cy][cx]+1
                    queue.append((nx,ny))
bfs()
print(maze[N-1][M-1])