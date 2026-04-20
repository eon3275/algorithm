class max_heap:
    def __init__(self):
        self.heap=[]
        self.cnt=0
    def push(self, value):
        self.heap.append(value)
        idx = self.cnt
        self.cnt+=1
        while idx>0:
            parent = (idx-1)//2
            if self.heap[parent]<self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break
    def pop(self):
        if self.cnt==0:
            return 0
        elif self.cnt==1:
            self.cnt-=1
            return self.heap.pop()
        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.cnt-=1
        root = 0
        while True:
            largest = root
            left = root*2+1
            right = root*2+2
            if left<self.cnt and self.heap[left]>self.heap[largest]:
                largest = left
            if right<self.cnt and self.heap[right]>self.heap[largest]:
                largest = right
            if largest!=root:
                self.heap[root], self.heap[largest] = self.heap[largest], self.heap[root]
                root = largest
            else:
                break
        return value
import sys
input = sys.stdin.readline
print = sys.stdout.write
heap = max_heap()
N = int(input())
for _ in range(N):
    x = -int(input().strip())
    if x==0:
        print(f'{-heap.pop()}\n')
    else:
        heap.push(x) 