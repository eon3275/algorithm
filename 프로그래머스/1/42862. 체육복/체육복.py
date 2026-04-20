def solution(n, lost, reserve):
    _lost = set(lost)-set(reserve)
    _reserve = set(reserve)-set(lost)
    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
    answer = n - len(_lost)
    return answer