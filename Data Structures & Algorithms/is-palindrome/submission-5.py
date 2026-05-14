class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        res = False
        while l < r:

            while r > l and not s[r].isalnum():
                r -= 1
            
            while l < r and not s[l].isalnum():
                l += 1
            print(s[r], s[l])
            if s[r].lower() != s[l].lower():
                return False
            else:
                res = True
            
            r -= 1
            l += 1
        
        return True
            