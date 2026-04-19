def solution(answers):
    answer = []
    patterns = [[1,2,3,4,5],[2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0,0,0]
    for i, ans in enumerate(answers):
        for idx, pattern in enumerate(patterns):
            if pattern[i%len(pattern)]==ans:
                scores[idx]+=1
    max_score = max(scores)
    
    return [i+1 for i, s in enumerate(scores) if max_score==s]