import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
heap = []
N = int(input())
for _ in range(N):
    n = int(input())
    if n==0: 
        if heap:
            print(f'{heapq.heappop(heap)[1]}\n')
        else:
            print('0\n')
    else:
        heapq.heappush(heap, [n if n>0 else -n, n])