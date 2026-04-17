import sys
input = sys.stdin.readline
N = int(input())
meetings = [list((map(int, input().strip().split()))) for _ in range(N)]
meetings.sort(key=lambda item: (item[1], item[0]))
cnt = 0
end = 0
for curr_start, curr_end in meetings:
    if end<=curr_start:
        cnt+=1
        start, end = curr_start, curr_end
print(cnt)