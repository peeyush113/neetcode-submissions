class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)        

        maxSeq = 0
        
        for n in nums:
            if (n-1) in numSet:
                continue
            length = 1
            while (n+length) in numSet:
                length += 1
            maxSeq = max(length, maxSeq)
        return maxSeq
