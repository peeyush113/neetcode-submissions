class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None: 

        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num*-1)
        diff = len(self.small) - len(self.large)
        if diff > 1:
            i = heapq.heappop(self.small)*-1
            heapq.heappush(self.large, i)
        elif diff < -1:
            i = heapq.heappop(self.large)
            heapq.heappush(self.small, i*-1)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.small[0]*-1 + self.large[0])/2
        elif len(self.small) > len(self.large):
            return self.small[0]*-1
        else:
            return self.large[0]


        