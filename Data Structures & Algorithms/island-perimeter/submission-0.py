class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        l, r = len(grid), len(grid[0])

        def dfs(i, j):
            if i<0 or j< 0 or i >= l or j >= r or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0

            visited.add((i, j ))

            return dfs(i+1, j) + dfs(i-1, j)+ dfs(i,j+1) + dfs(i, j-1)
        
        for i in range(l):
            for j in range(r):
                if grid[i][j]:
                    return dfs(i, j)
        return 0

                