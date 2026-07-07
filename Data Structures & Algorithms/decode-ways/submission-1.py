class Solution:
    def numDecodings(self, s: str) -> int:
        
        map = {str(n) for n in range(1, 27)}
        mem = {}
        def dfs(i):
            if i == len(s):
                return 1
            n = 0

            if i in mem:
                return mem[i]
            
            if s[i:i+1] in map:
                n += dfs(i+1)
            
            if i< len(s) and s[i:i+2] in map:
                n += dfs(i+2)
            mem[i] = n
            return mem[i]
        return dfs(0)
