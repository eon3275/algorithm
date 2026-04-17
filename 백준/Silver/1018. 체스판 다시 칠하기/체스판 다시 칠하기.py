N, M = map(int,input().split(' '))
matrix = []
best = 8*8
for _ in range(N):
    matrix.append(input())
for i in range(N-7):
    for j in range(M-7):
        case1 = 0
        case2 = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c)%2 ==  0:
                    if matrix[r][c] != 'W': case1 += 1
                    else: case2 += 1
                else:
                    if matrix[r][c] !='B': case1 += 1
                    else: case2 += 1
        best = min(best, case1, case2)
print(best)