word = input()
s = len(word)
for i in range(len(word)):
    if i+2 <= len(word)-1:
        if word[i]=='d' and word[i+1]=='z' and word[i+2]=='=':
            s-=1
    if i+1 <= len(word)-1:
        if word[i+1] == '=' or word[i+1] == '-':
            s-=1
        elif (word[i]=='l' or word[i]=='n') and word[i+1]=='j':
            s-=1
print(s)
