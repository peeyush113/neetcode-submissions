class Solution:
    def climbStairs(self, n: int) -> int:
        p, v = 1, 1
        for i in range(n-2, -1, -1):
            p, v = p+v, p
        return p