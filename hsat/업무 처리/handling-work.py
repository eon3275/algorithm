H, K, R = map(int, input().split())

tasks = [list(map(int, input().split()))[::-1] for _ in range(1 << H)]

# Please write your code here.
answer = 0
nodes = [[[],[]] for _ in range(1<<H)]
for d in range(R):
    today = d%2 # 1st(0) day is left, 2nd(1) day is right, 3rd(0) is left and so on
    if nodes[1][today]:
        answer+=nodes[1][today].pop(0)
    for i in range(2,1<<H):
        if nodes[i][today]:
            # even idx is left child
            nodes[i//2][i%2].append(nodes[i][today].pop(0))
    for i in range(1<<H):
        # leaf node work every day
        if tasks[i]:
            leaf_idx = (1<<H)+i
            nodes[leaf_idx//2][leaf_idx%2].append(tasks[i].pop())
print(answer)
