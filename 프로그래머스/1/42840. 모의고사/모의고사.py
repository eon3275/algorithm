def solution(answers):
    answer = []
    supo = [[[1,2,3,4,5],5,0],[[2,1,2,3,2,4,2,5], 8,0],[[3,3,1,1,2,2,4,4,5,5], 10, 0]]
    for i, ans in enumerate(answers):
        for sp in supo:
            if sp[0][i%sp[1]]==ans:
                sp[2]+=1
    max_correct = max(supo[0][2], supo[1][2], supo[2][2])
    for i in range(3):
        if max_correct==supo[i][2]:
            answer.append(i+1)
    return answer