class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, j):
            k, l = 0, 0
            for n in nums[i:j]:
                k, l = max(n+l, k), k
            return k
        
        return max(nums[0], dfs(0, len(nums)-1), dfs(1, len(nums)))