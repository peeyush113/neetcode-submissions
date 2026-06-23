class Solution:
    def hammingWeight(self, n: int) -> int:
        resp = 0
        while n:
            resp += n%2
            n = n//2
        return resp