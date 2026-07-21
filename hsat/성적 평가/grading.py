N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]

# Please write your code here.
total_score = [0]*N
for j in range(N):
    for i in range(3):
        total_score[j]+=scores[i][j]
scores.append(total_score)
for i in range(4):
    max_value = 3000 if i==3 else 1000
    cnt = [0]*(max_value+1)
    for score in scores[i]:
        cnt[score]+=1
    rank = [0]*(max_value+1)
    acc = 0
    for s in range(max_value,-1,-1):
        rank[s] = acc+1
        acc+=cnt[s]
    print(*(rank[s] for s in scores[i]))