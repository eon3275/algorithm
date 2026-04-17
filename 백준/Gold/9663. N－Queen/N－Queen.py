N = int(input())
cols = [True] * N
diag1 = [True] * (2*N-1)
diag2 = [True] * (2*N-1)

def backtracking(row):
    if row==N: return 1
    cnt = 0
    for col in range(N):
        if cols[col] and diag1[row-col+N-1] and diag2[row+col]:
            cols[col] = diag1[row-col+N-1] = diag2[row+col] = False
            cnt += backtracking(row+1)
            cols[col] = diag1[row-col+N-1] = diag2[row+col] = True
    return cnt

print(backtracking(0))
