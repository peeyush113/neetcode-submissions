class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = list(range(n))
        rank = [0] * n
        count = n
        def find(x):
            if x != parents[x]:
                parents[x]= find(parents[x])
            return parents[x]

        for x, y in edges:
            px, py = find(x), find(y)
            if px == py:
                return False

            if rank[px] > rank[py]:
                px, py  = py, px

            parents[py] = px 
            rank[px] += rank[py]
            count -= 1
        return count == 1