from collections import deque
import sys
input = sys.stdin.readline
N = int(input().strip())
queue = deque()
for _ in range(N):
    arg = list(input().strip().split())
    if arg[0] == 'push':
        queue.append(arg[1])
    elif arg[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif arg[0] == 'size':
        print(len(queue))
    elif arg[0] == 'empty':
        print(1 if not queue else 0)
    elif arg[0] == 'front':
        print(queue[0] if queue else -1)
    elif arg[0] == 'back':
        print(queue[-1] if queue else -1)