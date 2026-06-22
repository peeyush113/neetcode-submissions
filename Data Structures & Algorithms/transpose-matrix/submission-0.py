class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        resp = [[] for _ in range(col)]
        for c in range(col):
            for r in range(row):
                resp[c].append(matrix[r][c])
        return resp
            