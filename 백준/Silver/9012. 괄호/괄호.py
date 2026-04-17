import sys
input = sys.stdin.readline
def isVPS(string):
    stack = []
    for c in string:
        if c == '(':
            stack.append(c)
        else: #')'가 나오면
            if not stack:
                return False
            stack.pop()
    return len(stack)==0

strings = []
N = int(input())
for _ in range(N):
    strings.append(list(input().strip()))
for string in strings:
    if isVPS(string): print('YES')
    else: print('NO')