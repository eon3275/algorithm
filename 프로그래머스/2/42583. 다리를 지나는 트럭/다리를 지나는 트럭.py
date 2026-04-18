from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    limit=0 #weight
    bridge = deque([0]*bridge_length)
    while bridge:
        passed = bridge.popleft()
        limit -= passed
        if trucks:
            if limit+trucks[0]<=weight:
                enter = trucks.popleft()
                limit += enter
                bridge.append(enter)
            else:
                bridge.append(0)
        answer+=1
            
    return answer