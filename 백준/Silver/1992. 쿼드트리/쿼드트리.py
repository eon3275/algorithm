import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
pixel = [list(map(int, input().strip())) for _ in range(N)]
def solve(x,y,n):
    color = pixel[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if pixel[i][j]!=color:
                print('(')
                half = n//2
                solve(x,y,half)
                solve(x,y+half,half)
                solve(x+half,y,half)
                solve(x+half,y+half,half)
                print(')')
                return
    if color==0:
        print('0')
    else:
        print('1')

solve(0,0,N)