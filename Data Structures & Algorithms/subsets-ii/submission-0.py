class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        resp, op = [], []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                return resp.append(op.copy())
            
            op.append(nums[i])
            dfs(i+1)
            op.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return resp
