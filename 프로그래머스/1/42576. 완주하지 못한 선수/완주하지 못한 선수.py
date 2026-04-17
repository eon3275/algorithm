def solution(participant, completion):
    dicts = {}
    for p in participant:
        dicts[p] = dicts.get(p, 0)+1
    for c in completion:
        dicts[c]-=1
    for k in dicts:
        if dicts[k]>0:
            return k