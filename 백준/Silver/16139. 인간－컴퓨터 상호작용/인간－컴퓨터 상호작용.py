import sys
input = sys.stdin.readline
print = sys.stdout.write
S = list(input().strip())
q = int(input().strip())
N = len(S)
count = [[0]*(N+1) for _ in range(26)]
for i in range(N):
    idx = ord(S[i]) - ord('a')
    for j in range(26):
        count[j][i+1] = count[j][i]
    count[idx][i+1] += 1
result = []
for _ in range(q):
    a, l, r = input().strip().split()
    l, r = int(l), int(r)
    idx = ord(a) - ord('a')
    ans = count[idx][r+1]-count[idx][l]
    result.append(str(ans))
print('\n'.join(result)+'\n')