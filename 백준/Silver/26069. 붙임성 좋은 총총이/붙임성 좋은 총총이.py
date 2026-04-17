import sys
input = sys.stdin.readline
N = int(input())
ans = 0
S = set(['ChongChong'])
for _ in range(N):
    A, B = input().strip().split()
    if A in S or B in S:
        S.update([A, B])
print(len(S))