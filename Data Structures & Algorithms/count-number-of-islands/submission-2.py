class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r<0 or c<0 or r>=ROW or c>=COL or grid[r][c] == "0" or (r, c) in visited:
                return 0
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return 1
        count = 0
        for r in range(ROW):
            for c in range(COL):
                count += dfs(r, c)
        return count