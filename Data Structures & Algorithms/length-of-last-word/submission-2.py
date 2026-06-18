class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []

        w = ""
        for c in s:
            if c == " ":
                if w:
                    stack.append(w)
                w = ""
            else:
                w += c
        if w:
            stack.append(w)
            
        return len(stack[-1])