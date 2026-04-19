def solution(brown, yellow):
    wh = brown+yellow
    for i in range(3, int(wh**0.5)+1):
        if wh%i==0 and (2*(i+wh//i)-4)==brown:
            w = i
            h = wh//i
            break
    if w<h:
        w, h = h, w
    answer = [w, h]
    return answer