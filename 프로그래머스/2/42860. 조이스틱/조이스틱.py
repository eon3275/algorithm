def solution(name):
    up_down = 0
    for ch in name:
        moves = ord(ch)-ord('A')
        if moves>13:
            moves = 26-moves
        up_down+=moves
    n = len(name)
    left_right = n-1
    for i in range(n):
        next_idx = i+1
        while next_idx<n and name[next_idx]=='A':
            next_idx+=1
        left_right = min(left_right,i*2+(n-next_idx),2*(n-next_idx)+i)
    answer = up_down+left_right
    return answer