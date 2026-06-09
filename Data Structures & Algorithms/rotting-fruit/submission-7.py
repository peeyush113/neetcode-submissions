class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        queue = deque()
        fresh_count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1
        

        time = 0
        while queue and fresh_count >0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                    if min(dx, dy) <0 or dx>row-1 or dy>col-1:
                        continue

                    if grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        fresh_count -= 1
                        queue.append((dx, dy))
            time += 1
        return time if fresh_count ==0 else -1

        

