class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r<0 or c< 0 or r >=ROW or c>=COL or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            count = 1
            for d in [-1, 1]:
                count += dfs(r+d, c)
                count += dfs(r, c+d)
            return count
        max_iland = 0
        for i in range(ROW):
            for j in range(COL):
                if (i, j) not in visited:
                    max_iland = max(max_iland, dfs(i, j))
        return max_iland