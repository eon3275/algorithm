from collections import deque
def solution(n, computers):
    visited = [0]*n
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            q = deque([i])
            answer+=1
            while q:
                curr = q.popleft()
                for j in range(n):
                    if curr!=j and computers[curr][j] and not visited[j]:
                        visited[j] = 1
                        q.append(j)
    return answer