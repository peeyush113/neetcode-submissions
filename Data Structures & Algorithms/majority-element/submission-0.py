class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        m = len(nums)/2
        for n in nums:
            hash.setdefault(n, 0)
            hash[n] += 1
            if hash[n] > m:
                return n
                
            