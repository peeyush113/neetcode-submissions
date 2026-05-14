class Solution:
    def climbStairs(self, n: int) -> int:
        
        store = {}
        def fib(n):
            if n not in store:
                if n <=1:
                    op = 1
                else:
                    op = fib(n-1) + fib(n-2)
                store[n] = op
            else:
                op = store[n]
            return op
        return fib(n)