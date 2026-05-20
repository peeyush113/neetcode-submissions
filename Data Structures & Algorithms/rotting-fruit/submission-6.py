class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh, queue = 0, deque()
        for i in range(R):
            for j in range(C):
                v = grid[i][j]
                
                if v == 1:
                    fresh += 1
                elif v == 2:
                    queue.append((i, j))
                else:
                    continue
        minute = 0
        while fresh >0 and queue:
            
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if min(dr, dc) < 0 or dr >=R or dc>=C or grid[dr][dc] in [0, 2]:
                        continue
                    
                    grid[dr][dc] = 2
                    queue.append((dr, dc))
                    fresh -= 1
            minute += 1
        return minute if fresh == 0 else -1

        

