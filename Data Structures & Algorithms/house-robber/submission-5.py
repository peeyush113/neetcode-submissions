class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # def dfs(i):
        #     if i>= len(nums):
        #         return 0
            
        #     return max(dfs(i+1), nums[i]+dfs(i+2))
        # return dfs(0)

        rob1, rob2 = 0, 0

        for num in nums:
            rob1, rob2 = rob2, max(num + rob1, rob2)
        return rob2


