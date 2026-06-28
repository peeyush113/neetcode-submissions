class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, s):
            if i == len(nums):
                return s == target
            
            return dfs(i+1, s-nums[i]) + dfs(i+1, s+nums[i])
        return dfs(0, 0)