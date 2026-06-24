class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        resp = []
        def dfs(i, res):
            if i>= len(nums):
                resp.append(res.copy())
                return 
            res.append(nums[i])
            dfs(i+1, res)
            res.pop()
            dfs(i+1, res)
            
        dfs(0, [])
        return resp