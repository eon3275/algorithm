from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().strip().split())
field = [list(map(int, input().strip().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solve():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if field[i][j]==1:
                queue.append((j,i))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if field[ny][nx]==0:
                    field[ny][nx] = field[cy][cx]+1
                    queue.append((nx,ny))
    answer = 1
    for row in field:
        if 0 in row:
            return -1
        answer = max(answer, max(row))
    return answer-1
print(solve())