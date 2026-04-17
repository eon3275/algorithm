from collections import deque
N = int(input())
p = list(map(int, input().strip().split()))
q = deque(zip(range(1, N+1), p))
ans = []
while q:
    num, move = q.popleft()
    ans.append(str(num))
    if move>0:
        q.rotate(-(move-1))
    else:
        q.rotate(-move)
print(' '.join(ans))