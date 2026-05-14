class Solution:

    def squareSum(self, n:int)-> int:
        s = 0
        while n:
            reminder, n = n%10, n//10 
            s += reminder*reminder 
        return s

    def isHappy(self, n: int) -> bool:
        h = set()
        while True:
            s = self.squareSum(n)
            if s == 1:
                return True
            elif s in h:
                return False
            else:
                n = s
                h.add(s)