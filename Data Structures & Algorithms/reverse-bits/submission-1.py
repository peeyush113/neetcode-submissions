class Solution:
    def reverseBits(self, n: int) -> int:
        bin = []

        while n > 0:
            bin.append(n%2)
            n = n//2
        print(bin)
        resp = 0
        mul = pow(2, 31)
        for b in bin:
            resp += b*mul
            mul = mul//2
            print(resp, b, mul)
        return resp
