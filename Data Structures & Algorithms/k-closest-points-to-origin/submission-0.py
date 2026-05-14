import math

class MaxHeap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, distance, point):
        self.heap.append((distance, point))
        i = len(self.heap) -1
        p = i//2
        while i > 1 and self.heap[i][0] > self.heap[p][0]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[p]
            self.heap[p]= tmp
            i = p
            p = i//2

    def pop(self):
        if len(self.heap) ==1:
            return None
        if len(self.heap) ==2:
            return self.heap.pop()

        resp = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        l, r = i*2, i*2+1
        while l < len(self.heap):
            
            if (r < len(self.heap) 
                    and self.heap[l][0] < self.heap[r][0] 
                    and self.heap[i][0] < self.heap[r][0]):
                tmp = self.heap[r]
                self.heap[r] = self.heap[i]
                self.heap[i] = tmp
                i = r
            elif self.heap[i] < self.heap[l]:
                tmp = self.heap[l]
                self.heap[l] = self.heap[i]
                self.heap[i] = tmp
                i = l
            else:
                break
            l, r = i*2, i*2+1
        return resp

    @property
    def length(self):
        return len(self.heap)-1

    def top(self):
        return self.heap[1] if len(self.heap) > 1 else None


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = MaxHeap()
        for x, y in points:
            distance = math.sqrt(x*x+y*y)
            heap.push(distance, (x, y))
        print(heap.heap)
        if heap.length > k:
            for _ in range(heap.length-k):
                heap.pop()
        print(heap.heap)
        return [p[1] for p in heap.heap[1:]]








