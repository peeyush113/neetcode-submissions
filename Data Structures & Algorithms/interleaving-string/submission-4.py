class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if o != m+n:
            return False

        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[m][n] = True
        print(dp)
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                
                if i<m and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True

                if j < n and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]


        
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            k = i+j
            if k == len(s3):
                return (i == len(s1)) and j == len(s2)
            
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j):
                    cache[(i, j)] = True
                    return cache[(i, j)]

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1):
                    cache[(i, j)] = True
                    return cache[(i, j)]
            cache[(i, j)] = False
            return cache[(i, j)]
        return dfs(0, 0)