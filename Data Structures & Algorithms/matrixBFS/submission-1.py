class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = {(0, 0)}
        queue = deque()
        queue.append((0, 0))

        lenght = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROW-1 and  c== COL -1:
                    return lenght
                for dr, dc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:

                    if dr<0 or dc<0 or dr>=ROW or dc>= COL or grid[dr][dc] == 1 or (dr, dc) in visited:
                        continue
                    queue.append((dr,dc))
                    visited.add((dr, dc))
            lenght +=1 
        return -1

                