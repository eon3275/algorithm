from collections import deque
import sys
#input = sys.stdin.readline
N, M = map(int, input().strip().split())
jumps = {}
board = [-1]*101
for _ in range(N+M):
    x, y = map(int, input().strip().split())
    jumps[x] = y
def solve():
    queue = deque([1])
    board[1] = 0
    while queue:
        curr = queue.popleft()
        for d in range(1,7):
            nxt = curr+d
            if nxt<=100:
                nxt = jumps.get(nxt, nxt)
                if board[nxt]==-1:
                    board[nxt] = board[curr]+1
                    if nxt==100:
                        return board[100]
                    queue.append(nxt)
print(solve())