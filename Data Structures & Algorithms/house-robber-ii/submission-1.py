class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def dfs(i, j):
            k, l = 0, 0
            for n in nums[i:j]:
                k, l = max(n+l, k), k
            return k
        
        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))