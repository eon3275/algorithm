N = int(input())
dicts = {}
for _ in range(N):
    word = input()
    dicts[word] = len(word)
sorted_dict = sorted(dicts.items(), key= lambda item:(item[1], item[0]))
for word, length in sorted_dict:
    print(word)