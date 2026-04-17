import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
names = ['']*(N+1)
names_to_num = {}
for i in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    names[i] = name
    names_to_num[name] = i
for _ in range(M):
    stdin = sys.stdin.readline().rstrip()
    if stdin.isdigit():
        sys.stdout.write(names[int(stdin)]+'\n')
    else:
        sys.stdout.write(str(names_to_num[stdin])+'\n')