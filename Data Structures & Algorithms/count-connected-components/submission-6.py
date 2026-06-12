class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [0]*n
        count = n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return False
            
            # make px parent of py always and update rank of px to px+py
            # if rank of px is greater then py then flip them

            if rank[px] > rank[py]:
                px, py = py, px
            parents[py] = px
            rank[px] += rank[py]

            nonlocal count
            count -= 1
            return True
        
        for i, j in edges:
            union(i, j)
        print(parents)
        return count