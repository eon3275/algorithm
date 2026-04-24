from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().strip().split())
store = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]
def solve():
    queue = deque()
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if store[z][y][x]==1:
                    queue.append((z,y,x))
    while queue:
        cz,cy,cx = queue.popleft()
        for i in range(6):
            nz = cz+dz[i]
            ny = cy+dy[i]
            nx = cx+dx[i]
            if 0<=nz<H and 0<=ny<N and 0<=nx<M:
                if store[nz][ny][nx]==0:
                    store[nz][ny][nx] = store[cz][cy][cx]+1
                    queue.append((nz,ny,nx))
    answer = 0
    for floor in store:
        for row in floor:
            if 0 in row:
                return -1
            answer = max(answer, max(row))
    return answer-1
print(solve())