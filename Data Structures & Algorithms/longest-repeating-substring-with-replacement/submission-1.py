class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charHash = {}
        maxf = 0
        l = 0
        
        for r in range(len(s)):
            charHash[s[r]] = 1+charHash.get(s[r], 0)

            maxf = max(charHash[s[r]], maxf)
            
            if r-l+1 -maxf > k:
                charHash[s[l]] -= 1
                l += 1
            
        
        return r-l+1
                

