import sys
input = sys.stdin.readline
N = int(input())
queues = list(map(int, input().strip().split()))
queues.sort()
for i in range(1, N):
    queues[i] += queues[i-1]
print(sum(queues))