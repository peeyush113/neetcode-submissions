class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if i>=row or j >= col or i <0 or j <0 or grid[i][j] ==0:
                return 0
            
            visited.add((i, j))
            area = 1
            for k, l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (k, l) not in visited:
                    area += dfs(k, l)
            return area
        max_area = 0
        for i in range(row):
            for j in range(col):
                area = dfs(i, j)
                max_area = max(max_area, area)
        return max_area