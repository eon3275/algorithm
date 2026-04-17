import sys
input = sys.stdin.readline
stack = []
N = int(input())
args = [list(map(int, input().split())) for _ in range(N)]
for arg in args:
    if arg[0]==1:
        stack.append(arg[1])
    elif arg[0]==2:
        print(stack.pop() if stack else -1)
    elif arg[0]==3:
        print(len(stack))
    elif arg[0]==4:
        print(1 if not stack else 0)
    elif arg[0]==5:
        print(stack[-1] if stack else -1)