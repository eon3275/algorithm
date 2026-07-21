N = int(input())
scores = [[(val, i) for i, val in enumerate(map(int, input().split()))] for _ in range(3)]

# Please write your code here.
total_score = [0]*N
for j in range(N):
    for i in range(3):
        total_score[j] += scores[i][j][0]
    total_score[j] = (total_score[j], j)
scores.append(total_score)
for i in range(4):
    scores[i].sort(reverse=True)

ranks = [0]*N
for i in range(4):
    rank = 1
    prev_score = 1001
    for j in range(N):
        score, idx = scores[i][j]
        if score<prev_score:
            rank = j+1
        prev_score = score
        ranks[idx] = rank
    print(*ranks)
        