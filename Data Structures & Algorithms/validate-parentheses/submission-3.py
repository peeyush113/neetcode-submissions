class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}

        stack = []
        for b in s:
            if b not in brackets.keys():
                stack.append(b)
            else:                
                if not stack or stack[-1] != brackets[b]:
                    return False
                stack.pop()

        return len(stack) < 1