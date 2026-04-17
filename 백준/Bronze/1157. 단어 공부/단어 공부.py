word = input().upper()
wlist=list(set(word))
freq = []
for i in wlist:
    count = word.count(i)
    freq.append(count)
if freq.count(max(freq))==1:
    print(wlist[freq.index(max(freq))])
else :
    print('?')
