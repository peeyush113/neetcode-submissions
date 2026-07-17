class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = {}
        def dfs(t):
            if t == 0:
                return 1
            if t <0:
                return 0
            if t not in mem:
                resp = 0
                for n in nums:
                    resp += dfs(t-n)
                mem[t] = resp
            return mem[t]
        return dfs(target)