from collections import deque
N = int(input())
queue = deque([i for i in range(1, N+1)])
last = 1
while queue:
    last = queue.popleft()
    if queue:
        queue.append(queue.popleft())
print(last)