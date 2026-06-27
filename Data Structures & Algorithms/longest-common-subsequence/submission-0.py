class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        a, b = len(text1), len(text2)
        curr = [0]*(b+1)
        prev = [0]*(a+1)

        for i in range(a - 1, -1, -1):
            for j in range(b - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(curr[j+1], prev[j])
            prev, curr = curr, prev
        return prev[0]



        # def dfs(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     if text1[i] == text2[j]:
        #         return 1 + dfs(i+1, j+1)
        #     return max(dfs(i+1, j), dfs(i, j+1))
        # return dfs(0, 0)