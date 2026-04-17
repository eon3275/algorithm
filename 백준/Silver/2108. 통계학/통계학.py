import sys
input = sys.stdin.readline
data = list(map(int, sys.stdin.read().split()))
N = data[0]
data = sorted(data[1:])
dic = {}
for n in data:
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1
modes = []
maxfreq = max(dic.values())
for n in dic:
    if dic[n]==maxfreq:
        modes.append(n)
mean = sum(data)/N
print(int(mean+0.5) if mean>=0 else int(mean-0.5))
print(data[N//2])
print(modes[1] if len(modes)>1 else modes[0])
print(data[-1]-data[0])