class Solution:
    def numDecodings(self, s: str) -> int:
        
        map = {str(n) for n in range(1, 27)}
        m, n = 1, 0

        for i in range(len(s)-1, -1, -1):
            dp = 0
            if s[i] in map:
                dp = m 
            
            if s[i:i+2] in map:
                dp += n
            
            m, n = dp, m
        return m

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
