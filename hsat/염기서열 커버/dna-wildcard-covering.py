N, M = map(int, input().split())
sequences = [input() for _ in range(N)]

# Please write your code here.
incompat = [0]*N
for i in range(N):
    for j in range(N):
        comp = True
        for c in range(M):
            if (sequences[i][c]!='.' and sequences[j][c]!='.' and
                sequences[i][c]!=sequences[j][c]):
                comp = False
                break
        if not comp:
            incompat[i]|=1<<j
            incompat[j]|=1<<i
valid_mask = [False]*(1<<N)
valid_mask[0] = True
valid_lowest_bit = [[] for _ in range(N)]
for mask in range(1,1<<N):
    lowest_bit = mask&-mask
    i = lowest_bit.bit_length()-1
    rest = mask^lowest_bit
    if valid_mask[rest] and (rest&incompat[i])==0:
        valid_mask[mask] = True
        valid_lowest_bit[i].append(mask)
dp = [float('inf')]*(1<<N)
dp[0] = 0
for mask in range((1<<N)-1):
    if dp[mask]==float('inf'): continue
    for i in range(N):
        if not mask&(1<<i): break
    for v_mask in valid_lowest_bit[i]:
        n_mask = mask|v_mask
        if dp[n_mask]>dp[mask]+1:
            dp[n_mask] = dp[mask]+1
print(dp[(1<<N)-1])