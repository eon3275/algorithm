import heapq
import sys
input = sys.stdin.readline
N = int(input().strip())
heap = []
for i in range(N):
    for n in list(map(int, input().strip().split())):
        if len(heap)<N:
            heapq.heappush(heap, n)
        else:
            if heap[0]<n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
print(heap[0])
        