class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        mem = {}

        def dfs(a): 

            if a == 0:
                return 0

            if a in mem:
                return mem[a]

            m = float("inf")
            for c in coins:
                if a-c >= 0:
                    m = min(m, 1+dfs(a-c))
            mem[a] = m
            return mem[a]
        resp = dfs(amount)
        return -1 if resp == float("inf") else resp
