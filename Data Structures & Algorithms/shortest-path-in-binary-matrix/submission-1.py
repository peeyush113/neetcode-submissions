class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        visited = {(0, 0)}
        queue = deque()
        queue.append((0, 0))

        lenght = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if (r, c) == (n-1, n-1):
                    return lenght+1
                
                for k in [r+1, r, r-1]:
                    for l in [c+1, c , c-1]:
                        if (k, l) == (r, c) or min(k, l) < 0 or max(k, l) >= n or (k, l) in visited or grid[k][l] == 1:
                            continue
                        queue.append((k, l))
                        visited.add((k, l))
            lenght += 1
        return -1                
