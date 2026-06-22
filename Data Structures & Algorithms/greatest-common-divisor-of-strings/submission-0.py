class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def gcd(x, y):
            m = 0
            for i in range(1, x+1):
                if x%i == 0 and y%i == 0:
                    m = i 
            return m
        
        if str1 + str2 != str2 + str1:
            return ""
        
        g = gcd(len(str1), len(str2))
        print(g)
        return str1[:g]