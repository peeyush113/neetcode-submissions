class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r<0 or c<0 or r==R or c==C or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            return count
        
        maxCount = 0
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited or grid[r][c] == 1:
                    d = dfs(r, c)
                    maxCount = max(d, maxCount)
        return maxCount
