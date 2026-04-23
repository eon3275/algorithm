import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
N = int(input().strip())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    count=1
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    count+=1
                    queue.append((nx,ny))
    return count
answer = []
for x in range(N):
    for y in range(N):
        if not visited[x][y] and board[x][y]:
            answer.append(bfs(x,y))
answer.sort()
print(f'{len(answer)}\n')
for ans in answer:
    print(f'{ans}\n')