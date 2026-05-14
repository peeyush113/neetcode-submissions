class MinHeap:
    def __init__(self):
        self.heap = [float("-inf")]
    
    def push(self, val:int):
        self.heap.append(val)
        # percolate
        
        l = len(self.heap)-1
        m = l//2
        
        while self.heap[l] < self.heap[m]:
            tmp = self.heap[l]
            self.heap[l] = self.heap[m]
            self.heap[m] = tmp
            l = m
            m = l//2
            print("18", self.heap, l, m)

    def pop(self):
        resp = self.heap[1]

        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            l, r = 2*i, 2*i+1
            if r < len(self.heap) and self.heap[r] < self.heap[l] and self.heap[r] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[r]
                self.heap[r] = tmp
                i = r
            elif self.heap[l] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[l]
                self.heap[l] = tmp
                i = l
            else:
                break
        return resp

    @property
    def length(self):
        return len(self.heap)-1
    
    def top(self):
        return self.heap[1]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # keep an minHeap of lenght k 
        # pop smallest values if more then k values in heap
        # top most value will be kth largest value
        self.k = k
        self.heap = MinHeap()
        for n in nums:
            self.heap.push(n)
            print("58", n, self.heap.heap)
        print("59", self.heap.heap)
        while self.heap.length > self.k:
            self.heap.pop()
        print("62", self.heap.heap)

    def add(self, val: int) -> int:
        self.heap.push(val)
        if self.heap.length > self.k:
            self.heap.pop()
        print("68", self.heap.heap)
        return self.heap.top()
        
        

