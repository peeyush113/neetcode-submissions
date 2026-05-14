class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in nums]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c-1].append(n)

        resp = []
        l = len(freq) -1
        while l >= 0:
            for n in freq[l]:
                resp.append(n)
                if len(resp) == k:
                    return resp
            l -= 1  