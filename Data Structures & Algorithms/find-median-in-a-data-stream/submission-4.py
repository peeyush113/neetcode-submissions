class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:

        if self.high and num>self.high[0]:
            heapq.heappush(self.high, num)
        else:
            heapq.heappush(self.low, num*-1)
        
        if len(self.low) > len(self.high)+1:
            heapq.heappush(self.high, heapq.heappop(self.low)*-1)

        if len(self.high) > len(self.low)+1:
            heapq.heappush(self.low, heapq.heappop(self.high)*-1)            

    def findMedian(self) -> float:
        print(self.high, self.low)
        if len(self.high) > (len(self.low)):
            return self.high[0]
        elif len(self.high) < (len(self.low)): 
            return self.low[0]*-1
        else:
            return (self.high[0]+self.low[0]*-1)/2
        
        