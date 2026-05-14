class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = 0
        rowl, rowr = 0, len(matrix)-1
        while rowl <=rowr:
            m = (rowl+rowr)//2
            print(col, rowl, rowr, m)
            t = matrix[m][col]
            k = matrix[m][-1]
            if t <= target<=k:
                break
            elif target < t:
                rowr = m-1
            else:
                rowl = m+1
        print(f"col={col}, rowl={rowl}, rowr={rowr}, m={m}")
        row = m
        colr = len(matrix[0])-1
        while col<=colr:
            m = (col+colr)//2
            print(col, row, colr, m)
            t = matrix[row][m]
            if t == target:
                return True
            elif t > target:
                colr = m -1
            else:
                col = m+1
        return False