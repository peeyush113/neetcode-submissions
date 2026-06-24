class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        op = []

        def backtrack(i, resp):
            if len(resp) == k:
                op.append(resp.copy())
                return
            for j in range(i, n+1):
                resp.append(j)
                backtrack(j+1, resp)
                resp.pop()
        
        backtrack(1, [])
        return op