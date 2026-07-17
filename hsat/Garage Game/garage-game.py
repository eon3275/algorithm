from collections import deque
N = int(input())
colors = [list(map(int, input().split())) for _ in range(3 * N)]
# Please write your code here.
garage = [[0]*N for _ in range(N)]
next_cars = [deque([colors[i][j] for i in range(3*N-1,-1,-1)]) for j in range(N)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
def refresh(garage, next_cars):
    for i in range(N):
        remain = [c for c in garage[i] if c!=0]
        while len(remain)<N:
            remain.append(next_cars[i].popleft())
        garage[i] = remain
def backtracking(stage, score):
    if stage==3: return score
    refresh(garage, next_cars)
    visited = [[False]*N for _ in range(N)]
    curr_garage = [col.copy() for col in garage]
    curr_next_cars = [deque(dq) for dq in next_cars]
    max_score = score
    candidates = []
    def bfs(x,y,target):
        visited[x][y] = True
        coords = [(x,y)]
        q = deque([(x,y)])
        minx = maxx = x
        miny = maxy = y
        while q:
            cx,cy = q.popleft()
            for i in range(4):
                nx,ny = cx+dx[i], cy+dy[i]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and garage[nx][ny] == target:
                    visited[nx][ny] = True
                    minx,miny = min(minx,nx),min(miny,ny)
                    maxx,maxy = max(maxx,nx),max(maxy,ny)
                    q.append((nx,ny))
                    coords.append((nx,ny))
        score = len(coords)+(maxx-minx+1)*(maxy-miny+1)
        return score, coords
    for y in range(N):
        for x in range(N):
            if not visited[x][y]:
                local_score, local_candidates = bfs(x,y,garage[x][y])
                if local_score>2:
                    candidates.append((local_score, local_candidates))
    for curr_score, coords in candidates:
        for x,y in coords: garage[x][y] = 0
        max_score = max(max_score, backtracking(stage+1, score+curr_score))
        garage[:] = [col.copy() for col in curr_garage]
        next_cars[:] = [deque(dq) for dq in curr_next_cars]
    return max_score
print(backtracking(0,0))