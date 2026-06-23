class Solution:
    def oneBits(self, n):
        resp = 0
        while n:
            resp += n%2
            n = n//2
        return resp

    def countBits(self, n: int) -> List[int]:
        resp = []
        for i in range(n+1):
            resp.append(self.oneBits(i))
        return resp