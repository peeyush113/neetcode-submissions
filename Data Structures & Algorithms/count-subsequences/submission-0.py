class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]
                
                





        if len(t) > len(s):
            return 0

        def dfs(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0
            
            res = dfs(i+1, j)
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            return res
        return dfs(0, 0)