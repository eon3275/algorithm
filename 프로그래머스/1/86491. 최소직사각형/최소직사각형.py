def solution(sizes):
    w = h = 0
    for size in sizes:
        w = max(w, size[0] if size[0] > size[1] else size[1])
        h = max(h, size[1] if size[0] > size[1] else size[0])
    return w*h