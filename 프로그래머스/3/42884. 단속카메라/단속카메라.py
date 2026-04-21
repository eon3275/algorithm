def solution(routes):
    routes.sort(key=lambda x: x[1])
    print(routes)
    lastest = -30001
    answer = 0
    for s, e in routes:
        if s>lastest:
            answer+=1
            lastest = e
    return answer