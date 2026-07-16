from collections import deque
N, T = map(int, input().split())
signals = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(N)]
# Please write your code here.
dir_idx = {'R':0,'L':1,'U':2,'D':3}
dxdy = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
sig = {
    1 : ('R', ['U','R','D']),
    2 : ('U', ['L','U','R']),
    3 : ('L', ['U','L','D']),
    4 : ('D', ['L','D','R']),
    5 : ('R', ['U','R']),
    6 : ('U', ['L','U']),
    7 : ('L', ['L','D']),
    8 : ('D', ['D','R']),
    9 : ('R', ['R','D']),
    10: ('U', ['U','R']),
    11: ('L', ['U','L']),
    12: ('D', ['L','D'])
}
state = [[[[False]*4 for _ in range(4)] for _ in range(N)] for _ in range(N)]
visited = [[False]*N for _ in range(N)]
state[0][0][dir_idx['U']][0] = True
visited[0][0] = True
res = 1
q = deque([(0,0,'U',0)])
while q:
    x,y,prev_dir,t = q.popleft()
    if t==T: continue
    dir, next_dirs = sig[signals[x][y][t%4]]
    if prev_dir==dir:
        for next_dir in next_dirs:
            dx,dy = dxdy[next_dir]
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                if not state[nx][ny][dir_idx[next_dir]][(t+1)%4]:
                    state[nx][ny][dir_idx[next_dir]][(t+1)%4] = True
                    q.append((nx,ny,next_dir,t+1))
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        res+=1
print(res)