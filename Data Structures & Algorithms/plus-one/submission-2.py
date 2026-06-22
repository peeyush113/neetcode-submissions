class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        resp = []
        carry = 1
        for r in range(len(digits)-1, -1, -1):
            n = digits[r] + carry
            carry = n//10
            resp.append(n%10)
        if carry:
            resp.append(carry)
        op = []
        for i in range(len(resp)-1, -1, -1):
            op.append(resp[i])
        return op