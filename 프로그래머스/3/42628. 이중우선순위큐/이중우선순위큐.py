import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    valid = [False]*len(operations)
    for i, operation in enumerate(operations):
        op, num = operation.split()
        num = int(num)
        if op=='I':
            heapq.heappush(max_heap, (-num, i))
            heapq.heappush(min_heap, (num, i))
            valid[i] = True
        else:
            if num==1:
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, i = heapq.heappop(max_heap)
                    valid[i] = False
            else:
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, i = heapq.heappop(min_heap)
                    valid[i] = False
    while min_heap and not valid[min_heap[0][1]]: heapq.heappop(min_heap)
    while max_heap and not valid[max_heap[0][1]]: heapq.heappop(max_heap)
    
    if not min_heap:
        answer = [0, 0]
    else:
        answer = [-max_heap[0][0], min_heap[0][0]]
    
    return answer