N, M = map(int, input().split())
sequences = [input() for _ in range(N)]

# Please write your code here.

incompat = [0] * N
for i in range(N):
    for k in range(i + 1, N):
        comp = True
        for j in range(M):
            if (
                sequences[i][j] != "."
                and sequences[k][j] != "."
                and sequences[i][j] != sequences[k][j]
            ):
                comp = False
                break
        if not comp:
            incompat[i] |= 1 << k
            incompat[k] |= 1 << i

valid_mask_set = [False] * (1 << N)
valid_mask_set[0] = True
valid_by_lowest_bit = [[] for _ in range(N)]

for mask in range(1, 1 << N):
    low_bit = mask & -mask
    i = low_bit.bit_length() - 1
    rest = mask ^ low_bit

    if valid_mask_set[rest] and (incompat[i] & rest) == 0:
        valid_mask_set[mask] = True
        valid_by_lowest_bit[i].append(mask)

dp = [float("inf")] * (1 << N)
dp[0] = 0

for mask in range(1 << N):
    if dp[mask] == float("inf"):
        continue

    first_zero = -1
    for i in range(N):
        if not (mask & (1 << i)):
            first_zero = i
            break

    if first_zero == -1:
        continue

    for v_mask in valid_by_lowest_bit[first_zero]:
        next_mask = mask | v_mask
        if dp[next_mask] > dp[mask] + 1:
            dp[next_mask] = dp[mask] + 1

print(dp[(1 << N) - 1])