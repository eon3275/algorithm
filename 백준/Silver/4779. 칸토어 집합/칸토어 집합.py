import sys
input = sys.stdin.read
def ans(N):
    if len(N)<=1: return N
    n = len(N)//3
    N[n:2*n] = [' ']*n
    N[:n] = ans(N[:n])
    N[2*n:] = ans(N[2*n:])
    return N
    
def do(n):
    N = ['-']*(3**n)
    return ans(N)

data = list(map(int, input().strip().split()))

for i in data:
    print(''.join(do(i)))