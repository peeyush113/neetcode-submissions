class Solution:
    def addBinary(self, a: str, b: str) -> str:
        resp = ""
        l, r = len(a)-1, len(b)-1

        carry = 0
        while l>-1 or r>-1:
            if l>-1:
                carry += int(a[l])
                l -= 1
            if r > -1:
                carry += int(b[r])
                r -= 1
            print(l, r, carry)
            resp = str(carry%2) + resp
            carry = carry//2
        
        if carry:
            resp = str(carry) + resp
        return resp