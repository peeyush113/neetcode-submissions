class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        resp = 0
        for n in numSet:
            if n-1 not in numSet:
                l = 1
                while (n+l) in numSet:
                    l += 1
                resp = max(resp, l)
        return resp