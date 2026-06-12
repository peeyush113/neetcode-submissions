class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(n + 1))
        rank = [0]*(n + 1)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(i, j):
            px, py = find(i), find(j)

            if px == py:
                return False
            
            if rank[px] > rank[py]:
                parents[py] = px
            elif rank[px] < rank[py]:
                parents[px] = py
            else:
                parents[px] = py
                rank[py] += 1
            return True
        
        res = []
        for ex, ey in edges:
            if not union(ex, ey):
                res = [ex, ey]
        return res