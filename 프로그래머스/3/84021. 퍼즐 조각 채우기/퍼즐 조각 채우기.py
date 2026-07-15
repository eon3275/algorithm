from collections import deque
def norm(piece):
    min_x = min(p[0] for p in piece)
    min_y = min(p[1] for p in piece)
    new_piece = [(x-min_x, y-min_y) for x,y in piece]
    return sorted(new_piece)
def rotate(piece):
    new_piece = [(-y,x) for x,y in piece]
    return norm(new_piece)
def solution(game_board, table):
    blanks = []
    pieces = []
    n = len(game_board)
    def bfs(x,y,grid,target,mem):
        dx,dy = [1,-1,0,0],[0,0,1,-1]
        q = deque([(x,y)])
        grid[x][y] = -1
        piece = [(x,y)]
        while q:
            cx,cy = q.popleft()
            for i in range(4):
                nx,ny = cx+dx[i],cy+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if grid[nx][ny]==target:
                        grid[nx][ny] = -1
                        piece.append((nx,ny))
                        q.append((nx,ny))
        mem.append(piece)
    for i in range(n):
        for j in range(n):
            if game_board[i][j]==0:
                bfs(i,j,game_board,0,blanks)
            if table[i][j]==1:
                bfs(i,j,table,1,pieces)
    def match(blank):
        bn = norm(blank)
        for piece in pieces:
            if len(bn)!=len(piece): continue
            curr = norm(piece)
            for _ in range(4):
                if bn==curr:
                    pieces.remove(piece)
                    return len(curr)
                curr = rotate(curr)
        return 0
    answer = 0
    for blank in blanks:
        answer+=match(blank)
    return answer