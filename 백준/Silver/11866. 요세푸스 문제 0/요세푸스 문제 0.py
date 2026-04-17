import sys
from collections import deque
print = sys.stdout.write
N, K = map(int, input().split())
queue = deque(range(1, N+1))
ans = []
while queue:
    queue.rotate(-(K-1))
    ans.append(str(queue.popleft()))
print('<'+', '.join(ans)+'>\n')