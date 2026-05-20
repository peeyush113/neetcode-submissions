class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid)-1, len(grid[0])-1

        visited = set()
        def dfs(r,c ):
            if (r, c) in visited or min(r, c)<0 or r > ROW or c > COL or grid[r][c]==1:
                return 0
            if [r, c] == [ROW, COL]:
                return 1

            visited.add((r, c))

            count = 0
            count += dfs(r+1, c)
            count += dfs(r-1, c) 
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            visited.remove((r, c))
            return count

        return dfs(0, 0)
        


