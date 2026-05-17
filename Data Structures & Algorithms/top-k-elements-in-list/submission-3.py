class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map.setdefault(n, 0)
            map[n] += 1
        
        heap = []
        for key, val in map.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
                
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res