class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for b in s:
            if b in brackets.keys():
                stack.append(b)
            else:
                if len(stack) < 1:
                    return False
                a = stack.pop()
                if brackets[a] != b:
                    return False
        

        return len(stack) < 1