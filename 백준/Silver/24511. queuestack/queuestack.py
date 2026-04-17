from collections import deque
N = int(input())
qs = list(map(int, input().strip().split()))
value = list(map(int, input().strip().split()))
M = int(input())
C = list(map(int, input().strip().split()))
dq = deque()
ans = []
for i in range(N):
    if qs[i]==0:
        dq.appendleft(value[i])
for c in C:
    dq.append(c)
    ans.append(dq.popleft())
print(*ans)