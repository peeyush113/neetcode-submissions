class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = {x:[] for x in range(9)}
        boardHash = {}

        for r in range(9):
            row = []
            for c in range(9):
                print(r, c)
                v = board[r][c]
                if v == ".":
                    continue
                
                if v in row:
                    return False
                row.append(v)

                if v in col[c]:
                    return False
                col[c].append(v)
                
                k = f"{r//3}{c//3}"
                boardHash.setdefault(k, [])
                if v in boardHash[k]:
                    return False
                boardHash[k].append(v)
        
        return True