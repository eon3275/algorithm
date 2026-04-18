import heapq
from collections import deque
def solution(jobs):
    answer = 0
    N = len(jobs)
    count = 0
    now = 0
    waitings = []
    jobs = deque(sorted([[*job, i] for i, job in enumerate(jobs)]))
    while count<N:
        while jobs and jobs[0][0]<=now:
            starts, times, idx = jobs.popleft()
            heapq.heappush(waitings, [times, starts, idx])
        if waitings:
            time, starts, idx = heapq.heappop(waitings)
            now+=time
            count+=1
            answer += now-starts
        else:
            now = jobs[0][0]
    return answer//N

