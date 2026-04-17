import sys
data = input().split('-')
ans = sum(map(int, data[0].split('+')))
for num in data[1:]:
    ans-=sum(map(int, num.split('+')))
print(ans)