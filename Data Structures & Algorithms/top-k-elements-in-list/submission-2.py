class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        freqCount = [[]]
        for n in nums:
            hMap[n] = hMap.get(n, 0) + 1
            freqCount.append([])
        print(freqCount, hMap)
        for key, val in hMap.items():
            freqCount[val].append(key)

        
        resp = []
        for i in range(len(freqCount)-1, -1, -1):
            for n in freqCount[i]:
                resp.append(n)
                print(resp, i, n, k, len(resp))
                if len(resp) >= k:
                    return resp
                
        return resp