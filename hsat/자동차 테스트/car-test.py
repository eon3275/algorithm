n, q = map(int, input().split())
efficiency = list(map(int, input().split()))
m = [int(input()) for _ in range(q)]

# Please write your code here.
index = {}
efficiency.sort()
for i, e in enumerate(efficiency):
    index[e] = i
for m_i in m:
    if m_i not in index:
        print(0)
    else:
        less = index[m_i]
        print(less*(n-less-1))