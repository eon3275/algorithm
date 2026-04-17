numList = list()
for i in range(0, 9):
    numList.append(int(input()))
    
max = numList[0]

for j in range(9):
    if max<numList[j]:
        max = numList[j]

print(max)
print((numList.index(max))+1)