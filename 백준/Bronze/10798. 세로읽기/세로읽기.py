words = []
for _ in range(5):
    words.append(input())
max_index = 0
for i in range(5):
    if len(words[i])>max_index:
        max_index = len(words[i])
for i in range(max_index):
    for j in range(5):
        if i>=len(words[j]):
            continue
        print(words[j][i], end='')