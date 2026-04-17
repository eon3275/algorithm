N, M = map(int, input().split())
ans = []

def dfs(start, depth):
    if depth==M:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, N+1):
        ans.append(i)
        dfs(i+1, depth+1)
        ans.pop()
            
dfs(1, 0)