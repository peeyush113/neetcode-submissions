class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resp = ""
        while columnNumber>0:
            columnNumber -= 1
            resp = s[columnNumber%26] + resp
            columnNumber //= 26
        return resp