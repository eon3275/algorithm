from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
queue = deque([(0,0,0)])
visited[0][0][0] = 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    while queue:
        y,x,b = queue.popleft()
        if y==N-1 and x==M-1:
            return visited[y][x][b]
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=nx<M and 0<=ny<N:
                if maze[ny][nx]==0 and visited[ny][nx][b]==0:
                    visited[ny][nx][b] = visited[y][x][b]+1
                    queue.append((ny,nx,b))
                elif maze[ny][nx]==1 and b==0 and visited[ny][nx][1]==0:
                    visited[ny][nx][1] = visited[y][x][b]+1
                    queue.append((ny,nx,1))
    return -1
print(bfs())