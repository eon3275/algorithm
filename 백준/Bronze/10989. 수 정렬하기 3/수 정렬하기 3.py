import sys
numbers = [0]*10001
N = int(sys.stdin.readline().strip())
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    numbers[n] += 1
for i in range (1, 10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)