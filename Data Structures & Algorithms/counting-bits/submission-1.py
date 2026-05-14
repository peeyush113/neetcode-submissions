class Solution:
    def countBits(self, n: int) -> List[int]:
        resp = [0]*(n+1)

        for i in range(n+1):
            k = i
            c = 0
            if i%2 == 1:
                c += 1
            i = i >> 1
            c += resp[i]
            resp[k] = c
        return resp
