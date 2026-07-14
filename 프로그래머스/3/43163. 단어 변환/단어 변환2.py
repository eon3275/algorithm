from collections import defaultdict, deque
def solution(begin, target, words):
    if target not in words: return 0
    q = deque([(begin,0)])
    visited = set([begin])
    while q:
        word, step = q.popleft()
        if word==target:
            return step
        for nxt in words:
            if nxt not in visited:
                diff = sum(c1!=c2 for c1, c2 in zip(word, nxt))
                if diff==1:
                    visited.add(nxt)
                    q.append((nxt,step+1))
    return 0
