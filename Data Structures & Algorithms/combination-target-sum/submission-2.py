class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []
        def dfs(i, resp):

            if sum(resp) == target:
                op.append(resp.copy())
                return

            if i>= len(nums) or sum(resp) > target:
                return 
            
            
            resp.append(nums[i])
            dfs(i, resp)
            resp.pop()
            dfs(i+1, resp)

        dfs(0, [])
        return op
