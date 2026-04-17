N, M = map(int, input().split())
ans = []

def dfs(depth):
    if depth==M:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, N+1):
        ans.append(i)
        dfs(depth+1)
        ans.pop()
            
dfs(0)