class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        resp = []

        def backtrack(i, curr):
            if len(curr) >= k:
                resp.append(curr.copy())
                return
            
            if i >n :
                return

            for j in range(i, n+1):
                curr.append(j)
                backtrack(j+1, curr)
                curr.pop()
        backtrack(1, [])
        return resp

