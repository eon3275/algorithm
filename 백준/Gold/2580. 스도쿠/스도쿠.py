board = [list(map(int, input().split())) for _ in range(9)]
blanks = [(r, c) for r in range(9) for c in range(9) if board[r][c]==0]
rows = [[True]*10 for _ in range(9)]
cols = [[True]*10 for _ in range(9)]
square = [[True]*10 for _ in range(9)]
for r in range(9):
    for c in range(9):
        if board[r][c]!=0:
            n = board[r][c]
            rows[r][n] = cols[c][n] = square[r//3*3+c//3][n] = False
def dfs(i):
    if i == len(blanks):
        for line in board:
            print(*line)
        return True
    r, c = blanks[i]
    sq = r//3*3+c//3
    for n in range(1, 10):
        if rows[r][n] and cols[c][n] and square[sq][n]:
            rows[r][n] = cols[c][n] = square[sq][n] = False
            board[r][c] = n
            if dfs(i+1):
                return True
            rows[r][n] = cols[c][n] = square[sq][n] = True
            board[r][c] = 0
    return False

dfs(0)