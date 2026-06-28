class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
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