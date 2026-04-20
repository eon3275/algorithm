from collections import deque
def bfs(adj, start, ignore, n):
    visited = [False] * (n+1)
    visited[start] = visited[ignore] = True
    queue = deque([start])
    count = 1
    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count+=1
                queue.append(neighbor)
    return count
def solution(n, wires):
    answer = n
    adj = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        adj[v1].append(v2)
        adj[v2].append(v1)
    for v1, v2 in wires:
        count = bfs(adj, v1, v2, n)
        answer = min(answer, abs(count*2-n))
    return answer