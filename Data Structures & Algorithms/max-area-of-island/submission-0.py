class Solution:
    
    def dfs(self, r, c, grid, visited, rl, cl):
        if (r, c) in visited:
            return 0
        
        if r >= rl or r<0 or c<0 or c>=cl:
            return 0
        
        if grid[r][c] == 0:
            return 0
        
        island = 1
        visited.add((r,c))
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            island += self.dfs(r+dr, c+dc, grid, visited, rl, cl)
        return island

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rl, cl = len(grid), len(grid[0])
        visited = set()
        max_island = 0
        for r in range(rl):
            for c in range(cl):
                if (r, c) not in visited and grid[r][c] == 1:
                    island_len = self.dfs(r,c,grid, visited, rl, cl)
                    max_island = max(island_len, max_island)
        
        return max_island

