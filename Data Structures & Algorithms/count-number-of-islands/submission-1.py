class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            
            if r<0 or c<0 or r==R or c==C or (r, c) in visited:
                return 0
            
            if grid[r][c] == "0":
                return 0
            
            visited.add((r, c))

            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            
            return count
        
        islands = 0
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == "1":
                    d = dfs(r, c)
                    if d > 0:
                        islands += 1
        return islands