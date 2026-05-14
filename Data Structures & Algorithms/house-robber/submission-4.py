class Solution:
    def rob(self, nums: List[int]) -> int:
        r, b = 0, 0

        for n in nums:
            t = max(n+r, b)
            r = b
            b = t
        return b