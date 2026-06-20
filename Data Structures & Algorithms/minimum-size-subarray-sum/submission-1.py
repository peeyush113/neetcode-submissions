class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        window = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                window = min(window, r-l+1)
                total -= nums[l]
                l += 1
        return window if window != float("inf") else 0