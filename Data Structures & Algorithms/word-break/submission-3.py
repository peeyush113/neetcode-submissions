class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in mem:
                return mem[i]
                
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        mem[i] = True
                        return True
            mem[i] = False
            return False
        return dfs(0)
