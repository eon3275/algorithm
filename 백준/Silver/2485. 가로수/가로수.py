from math import gcd
import sys
input = sys.stdin.readline
N = int(input().rstrip())
gaps = []
trees = []

a = int(input().rstrip())
trees.append(a)
for _ in range(N-1):
    b = int(input().rstrip())
    gaps.append(b-a)
    trees.append(b)
    a = b
op = gcd(*gaps)
total = (trees[-1]-trees[0])//op+1
print(total-N)