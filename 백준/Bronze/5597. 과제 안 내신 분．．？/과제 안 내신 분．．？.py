arr = [i+1 for i in range(30)]
for _ in range(28):
    arr[int(input())-1] = 0
arr.sort()
print(arr[28])
print(arr[29])