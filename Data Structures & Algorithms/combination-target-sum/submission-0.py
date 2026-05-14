class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        op = []

        def sub(i, s):
            if s == target:
                res.append(op.copy())
                return

            if i >= len(nums) or s > target:
                return 
            
            op.append(nums[i])
            sub(i, s+nums[i])
            
            op.pop()
            sub(i+1, s)
        sub(0, 0)   
        return res 