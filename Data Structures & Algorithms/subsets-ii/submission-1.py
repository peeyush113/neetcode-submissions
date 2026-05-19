class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # practice with sort implementaion too

        resp = []

        def backtrack(i, curr):
            if i >= len(nums):
                resp.append(curr.copy())
                return 
            
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()

            while i+1< len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curr)
        backtrack(0, [])
        return resp



            