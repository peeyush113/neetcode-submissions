class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        col = len(matrix[0])-1
        row = 0
        while l<=r:
            m = (l+r)//2
            if target > matrix[m][col]:
                l = m+1
            elif target<matrix[m][0]:
                r = m-1
            else:
                row = m
                break
        arr = matrix[row]
        l, r = 0, len(arr)-1
        while l<=r:
            m = (l+r)//2
            if target>arr[m]:
                l = m+1
            elif target < arr[m]:
                r = m-1
            else:
                return True
        return False