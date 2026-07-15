from collections import defaultdict
def solution(tickets):
    adj = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        adj[src].append(dst)
    answer = []
    stack = ['ICN']
    while stack:
        curr = stack[-1]
        if not adj[curr]:
            answer.append(stack.pop())
        else:
            stack.append(adj[curr].pop())
    return answer[::-1]