class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        mem = {}
        def dfs(i):
            if i > len(nums):
                return 0

            if i not in mem:
                lis = 1
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        lis = max(lis, 1+dfs(j))
                mem[i] = lis
            return mem[i]
        
        return max(dfs(i) for i in range(len(nums)))
