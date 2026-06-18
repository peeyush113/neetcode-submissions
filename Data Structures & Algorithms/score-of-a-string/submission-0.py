class Solution:
    def scoreOfString(self, s: str) -> int:
        stack = []
        
        for i in range(len(s)-1):
            stack.append(abs(ord(s[i+1]) - ord(s[i])))
        
        return sum(stack)