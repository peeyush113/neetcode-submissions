class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        mem = {}

        def dfs(n, a): 

            if a== amount:
                return n

            if (n, a) in mem:
                return mem[(n, a)]

            m = float("inf")
            for c in coins:
                if c+a <= amount:
                    m = min(m, dfs(n+1, c+a))
            mem[(n, a)] = m
            return mem[(n, a)]
        resp = dfs(0, 0)
        return -1 if resp == float("inf") else resp
