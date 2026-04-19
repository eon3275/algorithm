from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for orders in permutations(dungeons, len(dungeons)):
        curr_k = k
        count = 0
        for o in orders:
            if curr_k>=o[0]:
                curr_k-=o[1]
                count+=1
            else:
                break
        answer = max(answer, count)
    return answer