class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]
        for num in nums:
            tmp = currMax * num
            cMin = num*currMin
            currMax = max(tmp, num*currMin, num)
            currMin = min(tmp, cMin, num)
            res = max(res, currMax)
        return res