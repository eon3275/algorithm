N = M = 9
List = []
for i in range(9):
    List.append(list(map(int, input().split())))
max, row, col = List[0][0], 0, 0
for i in range(9):
    for j in range(9):
        if max<List[i][j]:
            max = List[i][j]
            row = i
            col = j
print(max)
print(row+1, col+1)
