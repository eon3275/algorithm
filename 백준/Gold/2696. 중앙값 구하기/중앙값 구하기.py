import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    nums = []
    while len(nums)<N:
        nums.extend(list(map(int, input().strip().split())))
    max_l = []
    min_r = []
    ans = []
    for i in range(N):
        val = nums[i]
        if i%2==0:
            heapq.heappush(max_l, -val)
        else:
            heapq.heappush(min_r, val)
        if min_r and -max_l[0]>min_r[0]:
            left = -heapq.heappop(max_l)
            right = heapq.heappop(min_r)
            heapq.heappush(max_l, -right)
            heapq.heappush(min_r, left)
        if i%2==0:
            ans.append(-max_l[0])
    print(f'{(N+1)//2}\n')
    for i in range((N+1)//2):
        if i>0 and i%10==0:
            print('\n')
        print(f'{ans[i]} ')
    print('\n')