import sys
input = sys.stdin.readline
N = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(N)]
blue = white = 0
def solve(x, y, n):
    global blue, white
    color = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j]!=color:
                half = n//2
                solve(x,y,half)
                solve(x+half,y,half)
                solve(x,y+half,half)
                solve(x+half,y+half,half)
                return
    if color==0:
        white+=1
    else:
        blue+=1
solve(0,0,N)
print(white)
print(blue)