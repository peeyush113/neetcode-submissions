class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [float('-inf')]
        self.k = k
        for i in nums:
            self.add(i)

    def pop(self):
        if len(self.heap) ==1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i< len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[2*i+1] < self.heap[i]:
                j = 2*i+1
            elif self.heap[2*i] < self.heap[i]:
                j = 2*i
            else:
                break
            self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
            i = j
        return res

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap)-1
        p = i//2

        while self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i, p = p, p//2
        if len(self.heap)-1 > self.k:
            self.pop()        
        return self.heap[1]
