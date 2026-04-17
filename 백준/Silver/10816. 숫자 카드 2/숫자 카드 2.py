import sys
N = int(input())
n = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
m = list(map(int, sys.stdin.readline().rstrip().split()))
ans = {}
for i in n:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1
for i in m:
    if i in ans:
        print(ans[i], end=' ')
    else:
        print(0, end=' ')