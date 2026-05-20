class Solution:
    def isValid(self, s: str) -> bool:
        brakets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for b in s:
            if b in brakets.keys():
                stack.append(brakets[b])
            else:
                if not stack:
                    return False
                p = stack.pop()
                if b !=p:
                    return False
                
        return stack == []