N = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))
max_val = -1000000000
min_val = 1000000000
def dfs(depth, current, add, sub, mul, div):
    if depth==N:
        global max_val, min_val
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    if add>0:
        dfs(depth+1, current+numbers[depth], add-1, sub, mul, div)
    if sub>0:
        dfs(depth+1, current-numbers[depth], add, sub-1, mul, div)
    if mul>0:
        dfs(depth+1, current*numbers[depth], add, sub, mul-1, div)
    if div>0:
        dfs(depth+1, int(current/numbers[depth]), add, sub, mul, div-1)

dfs(1, numbers[0], *ops)
print(max_val)
print(min_val)

