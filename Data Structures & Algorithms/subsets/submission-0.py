class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        op = []
        def subset(i):
            if i >= len(nums):
                res.append(op.copy())
                return 
            
            subset(i+1)
            op.append(nums[i])
            subset(i+1)
            op.pop()
            
        subset(0)
        return res