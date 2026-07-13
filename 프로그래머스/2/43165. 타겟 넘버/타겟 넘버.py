from collections import deque
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    q = deque()
    q.append((0, 0))
    while q:
        i, curr = q.popleft()
        if i==n:
            if curr==target:
                answer+=1
            continue
        q.append((i+1, curr+numbers[i]))
        q.append((i+1, curr-numbers[i]))
    return answer