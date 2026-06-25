class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        resp = []
        perm = []
        count = {}
        for n in nums:
            count.setdefault(n, 0)
            count[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                resp.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
        dfs()
        return resp