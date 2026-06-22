class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            if n == 1 or n == 7:
                return True
            else:
                return False
        resp = 0
        while n > 0:
            c = n%10
            resp += c*c
            n = n//10
        return self.isHappy(resp)

