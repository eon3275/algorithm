from collections import deque
def solution(progresses, speeds):
    answer = []
    days = [(100-p+s-1)//s for p, s in zip(progresses, speeds)]
    release = 0
    for i in range(len(days)):
        if days[i] > days[release]:
            answer.append(i-release)
            release = i
    answer.append(len(days)-release)
    return answer