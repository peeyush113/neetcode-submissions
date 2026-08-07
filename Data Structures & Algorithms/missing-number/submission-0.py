class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum([n for n in range(0, len(nums)+1)])
        p = sum(nums)
        print(s, p)
        return s - p