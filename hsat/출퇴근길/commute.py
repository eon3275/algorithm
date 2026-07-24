from collections import defaultdict, deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
S, T = map(int, input().split())

# Please write your code here.
path = defaultdict(list)
r_path = defaultdict(list)
for src, dst in edges:
    path[src].append(dst)
    r_path[dst].append(src)
def bfs(start, graph, target=None):
    visited = [False]*(n+1)
    visited[start] = True
    q = deque([start])
    while q:
        curr = q.popleft()
        if target and curr==target: continue
        for nxt in graph[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return visited
s_t = bfs(S, path, T)
r_s_t = bfs(T, r_path)
t_s = bfs(T, path, S)
r_t_s = bfs(S, r_path)
answer = 0
for i in range(1,n+1):
    if i==S or i==T: continue
    if (s_t[i] and r_s_t[i] and t_s[i] and r_t_s[i]): answer+=1
print(answer)