num = list(map(int, input()))
num.sort(reverse=True)
print(*num, sep='')