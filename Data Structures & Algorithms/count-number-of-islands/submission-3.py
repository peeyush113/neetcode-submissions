class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        n = row*col
        parents = [i for i in range(n)]
        rank = [0 for i in range(n)]

        ilands_merged = 0

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] > rank[py]:
                px, py = py, px
            parents[py] = px
            rank[px] += rank[py]
            nonlocal ilands_merged
            ilands_merged +=1
            return True

        visited = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    for x, y in [(i+1, j), (i-1, j), (i,j+1), (i, j-1)]:
                        if min(x, y) <0 or x>row-1 or y > col-1 or grid[x][y] == "0":
                            continue
                        union(i*col+j, x*col+y)
        return len(visited) - ilands_merged
