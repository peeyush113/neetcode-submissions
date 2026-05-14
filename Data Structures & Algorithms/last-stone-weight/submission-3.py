class MaxHeap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, val:int):
        self.heap.append(val)
        i = len(self.heap)-1
        p = i//2
        while i>1 and self.heap[i] > self.heap[p]:
            tmp = self.heap[p]
            self.heap[p] = self.heap[i]
            self.heap[i] = tmp
            i = p
            p = i//2
    
    @property
    def length(self):
        return len(self.heap)-1

    def pop(self):
        if len(self.heap) ==1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        resp = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            l, r = 2*i, 2*i+1
            if r<len(self.heap) and self.heap[r] > self.heap[l] and self.heap[i] < self.heap[r]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[r]
                self.heap[r] = tmp
                i = r
            elif self.heap[i] < self.heap[l]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[l]
                self.heap[l] = tmp
                i = l
            else:
                break
        return resp

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        for s in stones:
            heap.push(s)
        
        print(heap.heap)
        while heap.length > 1:
            x = heap.pop()
            y = heap.pop()
            
            x, y = x-y, y-x             
            
            if x>0:
                heap.push(x)
            if y>0:
                heap.push(y)
        
        print(heap.heap)
        if heap.length >0:
            return heap.pop()
        return 0








        