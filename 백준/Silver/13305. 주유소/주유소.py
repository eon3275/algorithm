N = int(input())
roads = list(map(int, input().split()))+[0]
cities = list(map(int, input().split()))
ans = 0
curr_min = float('inf')
for v, e in zip(cities, roads):
    if v<curr_min:
        curr_min = v
    ans += curr_min*e
print(0 if N==1 else ans)