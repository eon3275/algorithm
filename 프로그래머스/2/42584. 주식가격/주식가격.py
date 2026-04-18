def solution(prices):
    N = len(prices)
    answer = [0]*N
    stack = []
    for i in range(N):
        while stack and prices[i]<prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i-top
        stack.append(i)
    while stack:
        top = stack.pop()
        answer[top] = N-1-top
    return answer