import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().strip().split())) for _ in range(N)]
n_ones = zeros = ones = 0
def solve(x,y,n):
    global n_ones, zeros, ones
    num = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j]!=num:
                div = n//3
                solve(x,y,div)
                solve(x,y+div,div)
                solve(x,y+div*2,div)
                solve(x+div,y,div)
                solve(x+div,y+div,div)
                solve(x+div,y+div*2,div)
                solve(x+div*2,y,div)
                solve(x+div*2,y+div,div)
                solve(x+div*2,y+div*2,div)
                return
    if num==-1:
        n_ones+=1
    elif num==0:
        zeros+=1
    else:
        ones+=1
solve(0,0,N)
print(n_ones, zeros, ones, sep='\n')