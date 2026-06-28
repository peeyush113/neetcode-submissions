class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i==len(word1) and j < len(word2):
                cache[(i, j)] = len(word2[j:])
                return cache[(i, j)]
            
            if j == len(word2) and i<len(word1):
                cache[(i, j)] = len(word1[i:])
                return cache[(i, j)]

            if i == len(word1) and j == len(word2):
                cache[(i, j)] = 0
                return cache[(i, j)]
            
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]      
            cache[(i, j)] = min(1+dfs(i+1, j), 1+dfs(i+1, j+1), 1+dfs(i, j+1))
            return cache[(i, j)]
        
        return dfs(0, 0)
            
