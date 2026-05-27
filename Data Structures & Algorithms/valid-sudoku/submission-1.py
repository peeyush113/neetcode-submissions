class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, sq = defaultdict(set),  defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                b = board[r][c]
                if b == ".":
                    continue
                
                if b in row[r] or b in col[c] or b in sq[(r//3, c//3)]:
                    return False
                col[c].add(b)
                row[r].add(b)
                sq[(r//3, c//3)].add(b)
        return True