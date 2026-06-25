class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[r-1][c-1] == 1:
            return 0

        prevRow = [0] *c

        for row in range(r-1, -1, -1):
            currRow = [0] * c
            if row == r-1:
                currRow[-1] = 1
            else:
                currRow[-1] = prevRow[-1] if obstacleGrid[row][c-1] == 0 else 0

            for col in range(c-2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    currRow[col] = 0
                    continue
                    
                currRow[col]  = prevRow[col] + currRow[col+1]
            print(currRow, prevRow, row)
            prevRow = currRow
        return prevRow[0]
