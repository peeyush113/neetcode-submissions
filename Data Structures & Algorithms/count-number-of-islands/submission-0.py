class Solution:
    def dfs(self, r,c, grid, visited, row_len, col_len):
        
        print(r, c, row_len, col_len)
        
        if (r, c) in visited:
            return

        if r>=row_len or r<0 or c>=col_len or c<0:
            return

        if grid[r][c] == "0":
            return
                
        visited.add((r, c))
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            self.dfs(r+dr, c+dc, grid, visited, row_len, col_len)
        return


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands = 0
        visited = set()
        r_len, c_len = len(grid), len(grid[0])

        for r in range(r_len):
            for c in range(c_len):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    self.dfs(r, c, grid, visited, r_len, c_len)
        return islands
                


