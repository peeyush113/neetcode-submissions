class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        cache = {}
        def dfs(i, m, n):
            if i == len(nums):
                return m == n

            if (i, m, n) in cache:
                return cache[(i, m, n)]

            num = nums[i]
            cache[(i, m, n)] = dfs(i+1, m+num, n) or dfs(i+1, m, n+num)
            return cache[(i, m, n)]
        return dfs(0, 0, 0)
