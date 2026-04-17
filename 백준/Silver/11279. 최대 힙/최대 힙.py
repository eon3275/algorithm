import sys
input = sys.stdin.readline
print = sys.stdout.write
class Heap:
    def __init__(self):
        self.heap=[]
        self.cnt=0
    def push(self, val):
        self.heap.append(val)
        self.cnt+=1
        self._heapify_up(self.cnt-1)
    def pop(self):
        if self.cnt==0:
            return 0
        elif self.cnt==1:
            self.cnt-=1
            return self.heap.pop()
        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.cnt-=1
        self._heapify_down(0)
        return val
    def _heapify_up(self, idx):
        while idx>0:
            parent = (idx-1)//2
            if self.heap[idx]>self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break
    def _heapify_down(self, idx):
        while True:
            largest = idx
            left = idx*2+1
            right = idx*2+2
            if left<self.cnt and self.heap[left]>self.heap[largest]:
                largest = left
            if right<self.cnt and self.heap[right]>self.heap[largest]:
                largest = right
            if largest!=idx:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                idx = largest
            else:
                break
heap = Heap()
N = int(input())
for _ in range(N):
    x = int(input().strip())
    if x==0:
        print(f'{heap.pop()}\n')
    else:
        heap.push(x)    