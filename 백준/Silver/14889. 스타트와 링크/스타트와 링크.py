import sys
from itertools import combinations
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')
members = list(range(1, N))
S = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        S[i][j] = numbers[i][j]+numbers[j][i]

for start in combinations(members, N//2-1):
    start = list(start)+[0]
    link = list(set(range(N))-set(start))
    start_sum = 0
    for i, j in combinations(start, 2):
        start_sum+=S[i][j]
    link_sum=0
    for i, j in combinations(link, 2):
        link_sum+=S[i][j]
    diff = abs(start_sum-link_sum)
    if diff<min_diff:
        min_diff = diff
    if min_diff==0:
        break

print(min_diff)
