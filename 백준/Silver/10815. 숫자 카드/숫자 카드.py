import sys
N = int(input())
n = list(map(int, sys.stdin.readline().split()))
n = set(n)
M = int(input())
m = list(map(int, sys.stdin.readline().split()))
for num in m:
    if num in n:
        print('1', end=' ')
    else:
        print('0', end=' ')