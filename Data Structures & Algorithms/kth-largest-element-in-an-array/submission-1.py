class Heap:

    def __init__(self, k) -> None:
        self.heap = [0]
        self.k = k+1

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) -1
        p = i//2

        while p> 0 and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i] 
            i, p = p, p//2
        
        if len(self.heap)>self.k:
            self.pop()
    
    def pop(self):
        if len(self.heap) ==1:
            return None
        if len(self.heap) ==2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        l, r = 2*i, 2*i+1

        while l < len(self.heap):
            if r< len(self.heap) and self.heap[i] > self.heap[r] and self.heap[l] > self.heap[r]:
                j = r
            elif self.heap[i] > self.heap[l]:
                j = l
            else:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j 
            l, r = 2*i, 2*i+1
        return res
            

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap(k)
        for n in nums:
            heap.push(n)
        print(heap.heap)
        return heap.pop()


        