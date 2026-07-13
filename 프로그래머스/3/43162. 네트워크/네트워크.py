def solution(n, computers):
    parent = [i for i in range(n)]
    size = [1]*n
    def find(node):
        while node!=parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    def union(u, v):
        pu = find(u)
        pv = find(v)
        if pu!=pv:
            if size[pv]>size[pu]:
                pu, pv = pv, pu
            parent[pv] = pu
            size[pu]+=size[pv]
            return 1
        return 0
    answer = n
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]==1: 
                answer -= union(i,j)
    return answer