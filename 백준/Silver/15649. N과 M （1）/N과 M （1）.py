N, M = map(int, input().split())
ans = []

def backtracking():
    if len(ans)==M:
        print(' '.join(map(str, ans)))

    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            backtracking()
            ans.pop()
backtracking()