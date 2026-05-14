class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh, time = 0, 0
        rl = [x for x in range(len(grid))]
        cl = [x for x in range(len(grid[0]))]

        for r in rl:
            for c in cl:
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in rl and nc in cl and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1
            print(time, fresh, queue)

        return time if fresh ==0 else -1 
