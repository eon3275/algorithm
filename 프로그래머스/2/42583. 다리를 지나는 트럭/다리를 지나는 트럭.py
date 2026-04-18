from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque()
    curr_weight = 0
    while trucks or bridge:
        answer+=1
        if bridge and bridge[0][1] == answer:
            t_w, _ = bridge.popleft()
            curr_weight -= t_w
        if trucks and trucks[0]+curr_weight <= weight:
            t_w = trucks.popleft()
            curr_weight += t_w
            bridge.append((t_w, answer+bridge_length))
        elif bridge:
            if answer<bridge[0][1]-1:
                answer = bridge[0][1]-1
            
    return answer