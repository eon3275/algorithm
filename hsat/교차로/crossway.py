N = int(input())
t = []
w = []

for _ in range(N):
    time, pos = input().split()
    t.append(int(time))
    w.append(pos)

# Please write your code here.
roads = [[] for _ in range(4)]
for i in range(N-1,-1,-1):
    roads[ord(w[i])-ord('A')].append((t[i],i))
def is_blanked():
    for i in range(4):
        if roads[i]: return False
    return True
def deadlock(curr_time):
    cnt = 0
    for i in range(4):
        if roads[i] and curr_time>=roads[i][-1][0]:
            cnt+=1
    return cnt==4
def timejump(curr_time):
    next_time = float('inf')
    for i in range(4):
        if roads[i]: next_time = min(next_time, roads[i][-1][0])
    return next_time
answer = [-1]*N
time = 0
while True:
    if is_blanked(): break
    passed = [0]*4
    for i in range(4):
        if roads[i] and time>=roads[i][-1][0]:
            if not roads[i-1] or time<roads[i-1][-1][0]:
                passed[i] = 1
    if sum(passed)>0:
        for i in range(4):
            if passed[i]:
                answer[roads[i].pop()[1]] = time
        time+=1
    else:
        if deadlock(time): break
        time = timejump(time)
print('\n'.join(map(str, answer)))