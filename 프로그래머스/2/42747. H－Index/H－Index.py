def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, cite in enumerate(citations):
        if cite < i+1:
            return i
    return len(citations)