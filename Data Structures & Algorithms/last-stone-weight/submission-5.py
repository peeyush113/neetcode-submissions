class Heap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, x):
        self.heap.append(x)
        i = len(self.heap) -1
        p = i//2

        while p>0 and self.heap[i] > self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i, p = p, p//2
    
    def pop(self):
        
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]    
        self.heap[1] = self.heap.pop()
        i = 1
        l, r = 2*i, 2*i +1

        while l < len(self.heap):
            if (r < len(self.heap) and self.heap[r] > self.heap[l] 
                and self.heap[r] > self.heap[i]):
                j = r
            elif self.heap[l] > self.heap[i]:
                j = l
            else: 
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
            l, r = 2*i, 2*i +1
        return res

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = Heap()
        for x in stones:
            heap.push(x)
        
        while len(heap.heap) > 2:
            res = heap.pop() - heap.pop()
            print(heap.heap)
            if res>0:
                heap.push(res)
                print(heap.heap)
        return heap.pop() if len(heap.heap) ==2 else 0


        