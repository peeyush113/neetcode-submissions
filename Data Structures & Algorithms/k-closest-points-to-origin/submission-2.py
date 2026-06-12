class Heap:

    def __init__(self, k) -> None:
        self.heap = [(0, [0, 0])]
        self.k = k+1
    
    def push(self, distance, point):
        self.heap.append((distance, point))
        i = len(self.heap)-1
        p = i//2
        while p>0 and self.heap[i][0]>self.heap[p][0]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i, p = p, p//2
        
        if len(self.heap) > self.k:
            self.pop()

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        l, r = i*2, i*2+1

        while l < len(self.heap):
            if r<len(self.heap) and self.heap[r][0] > self.heap[i][0] and self.heap[r][0] > self.heap[l][0]:
                j = r
            elif self.heap[l][0] > self.heap[i][0]:
                j = l
            else:
                break

            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
            l, r = i*2, i*2+1
        return res

    def all_points(self):
        res = []
        for d, p in self.heap[1:]:
            res.append(p)
        return res

class Solution:

    def distance(self, point):
        x, y = point
        return math.sqrt(x*x+y*y)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = Heap(k)
        for p in points:
            distance = self.distance(p)
            heap.push(distance, p)
        
        return heap.all_points()




