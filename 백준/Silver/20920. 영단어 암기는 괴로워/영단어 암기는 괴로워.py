import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().rstrip().split())
dicts = {}
for _ in range(N):
    word = input().rstrip()
    if len(word)<M: continue
    if word in dicts:
        dicts[word]+=1
    else:
        dicts[word]=1
ans = sorted(dicts, key = lambda x: (-dicts[x], -len(x), x))
print('\n'.join(ans)+'\n')