from math import gcd
import sys
input = sys.stdin.readline
def isprime(x):
    if x<2: return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

N = int(input().rstrip())
nums = []
for _ in range(N):
    nums.append(int(input().rstrip()))
for num in nums:
    while True:
        if isprime(num):
            print(num)
            break
        num+=1