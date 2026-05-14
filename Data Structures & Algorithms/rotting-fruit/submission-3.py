class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        freshOranges = set()
        rottenOranges = []
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    freshOranges.add((r, c))
                elif grid[r][c] == 2:
                    rottenOranges.append((r, c))
                else:
                    pass
        
        minutes = 0
        if not freshOranges:
            return minutes

        while rottenOranges:
            if not freshOranges:
                return minutes
            
            for _ in range(len(rottenOranges)):    
                r, c = rottenOranges.pop(0)
                
                for x, y in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if x<0 or y<0 or x==R or y==C or grid[x][y] != 1:
                        continue
                    grid[x][y] = 2
                    freshOranges.remove((x,y))
                    rottenOranges.append((x, y))
                print((r, c), minutes, freshOranges, grid)
            minutes += 1
            print(minutes, freshOranges, grid)
    
        return -1

