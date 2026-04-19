def solution(brown, yellow):
    wh = brown+yellow
    for h in range(3, int(wh**0.5)+1):
        if wh%h==0:
            w = wh//h
            if (w-2)*(h-2) == yellow:
                return [w, h]
    return answer