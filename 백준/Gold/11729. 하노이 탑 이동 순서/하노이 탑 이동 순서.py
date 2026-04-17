import sys
print = sys.stdout.write
def hanoi(N, start, end, mid):
    if N==1:
        print(f'{start} {end}\n')
        return
    hanoi(N-1, start, mid, end)
    print(f'{start} {end}\n')
    hanoi(N-1, mid, end, start)

N = int(input())
print(f'{2**N-1}\n')
hanoi(N, 1, 3, 2)