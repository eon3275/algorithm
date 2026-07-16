from collections import deque
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
# Please write your code here.
directions = ['<','^','>','v']
dr = [0,-1,0,1]
dc = [-1,0,1,0]
def find_init():
    for r in range(H-1,-1,-1):
        for c in range(W-1,-1,-1):
            if grid[r][c]=='#':
                path = 0
                for i in range(4):
                    nr,nc = r+dr[i], c+dc[i]
                    if 0<=nr<H and 0<=nc<W and grid[nr][nc]=='#':
                        path+=1
                        path_dir = i
                if path==1:
                    return (r,c,path_dir)
sr, sc, sdir = find_init()
grid[sr][sc] = '.'
print(sr+1, sc+1)
print(directions[sdir])
q = deque([(sr,sc,sdir)])
command = ''
while q:
    r,c,d = q.popleft()
    for i in range(-1,2):
        nd = (d+i)%4
        nr1,nc1 = r+dr[nd], c+dc[nd]
        nr2,nc2 = r+2*dr[nd], c+2*dc[nd]
        if 0<=nr2<H and 0<=nc2<W and grid[nr1][nc1]==grid[nr2][nc2]=='#':
            grid[nr1][nc1]=grid[nr2][nc2]='.'
            q.append((nr2,nc2,nd))
            command+='L' if i==-1 else 'R' if i==1 else ''
            command+='A'
            break
print(command)