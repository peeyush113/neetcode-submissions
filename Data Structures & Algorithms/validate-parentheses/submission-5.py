class Solution:
    def isValid(self, s: str) -> bool:
        brakets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for b in s:
            if b in brakets.keys():
                stack.append(brakets[b])
            else:
                if stack and b == stack.pop():
                    continue
                else:
                    return False
                
        return stack == []