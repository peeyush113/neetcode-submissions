class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resp = []

        def backtrack(i, cur):
            if sum(cur) > target:
                return
            
            if sum(cur) == target:
                resp.append(cur.copy())
                return
                        
            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtrack(j,  cur)
                cur.pop()
        
        backtrack(0, [])
        return resp