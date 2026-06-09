class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])

        INF = 2147483647
        


        def bfs(r, c):
            queue = deque()
            queue.append((r, c))    
            visited = [[False]*col for j in range(row)]
            visited[r][c] = True
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    if grid[i][j] == 0:
                        return steps
                    
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if not (x<0 or y<0 or x>row-1 or y>col-1 or grid[x][y] == -1 or visited[x][y]):
                            visited[x][y] = True
                            queue.append((x, y))
                steps += 1
            return INF
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)