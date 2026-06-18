class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
                continue
            
            st = ""
            con = ""
            while stack[-1] != "[":
                st = stack.pop()+st

            stack.pop()
            while stack and stack[-1].isdigit():
                con = stack.pop() + con
            stack.append(int(con)*st)
        return "".join(stack)
        