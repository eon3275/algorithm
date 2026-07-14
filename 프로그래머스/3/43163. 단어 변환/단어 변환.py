from collections import defaultdict, deque
def solution(begin, target, words):
    if target not in words: return 0
    words.append(begin)
    patterns = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            pattern = word[:i]+'*'+word[i+1:]
            patterns[pattern].append(word)
    q = deque([(begin,0)])
    visited = set([begin])
    while q:
        word, step = q.popleft()
        if word==target:
            return step
        for i in range(len(word)):
            pattern = word[:i]+'*'+word[i+1:]
            for nxt in patterns[pattern]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt,step+1))
    return 0
