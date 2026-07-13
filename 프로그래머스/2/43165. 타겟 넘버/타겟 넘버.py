def solution(numbers, target):
    n = len(numbers)
    def dfs(i, curr):
        if i==n:
            return 1 if curr==target else 0
        return dfs(i+1, curr+numbers[i])+dfs(i+1, curr-numbers[i])
    return dfs(0,0)
