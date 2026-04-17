import sys
from collections import deque
print = sys.stdout.write
input = sys.stdin.readline
N = int(input().strip())
deque = deque()
for _ in range(N):
    args = list(map(int, input().strip().split()))
    if args[0]==1:
        deque.appendleft(args[1])
    elif args[0]==2:
        deque.append(args[1])
    elif args[0]==3:
        print(f'{deque.popleft() if deque else -1}\n')
    elif args[0]==4:
        print(f'{deque.pop() if deque else -1}\n')
    elif args[0]==5:
        print(f'{len(deque)}\n')
    elif args[0]==6:
        print(f'{1 if not deque else 0}\n')
    elif args[0]==7:
        print(f'{deque[0] if deque else -1}\n')
    elif args[0]==8:
        print(f'{deque[-1] if deque else -1}\n')