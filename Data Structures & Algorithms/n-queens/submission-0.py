class Board:

    def __init__(self, n) -> None:
        self.state = [["."]*n for _ in range(n)]
        self.dig = set()
        self.cols = set()
        self.aDig = set()
    
    def get_state(self):
        resp = ["".join(row) for row in self.state]
        return resp
    
    def in_col(self, row, col):
        d = row-col
        ad = row+col
        return col in self.cols or d in self.dig or ad in self.aDig
    
    def add_col(self, row, col):
        d = row-col
        ad = row+col
        self.dig.add(d)
        self.aDig.add(ad)
        self.cols.add(col)
        self.state[row][col] = "Q"
    
    def remove_col(self, row, col):
        d = row-col
        ad = row+col
        self.dig.remove(d)
        self.aDig.remove(ad)
        self.cols.remove(col)
        self.state[row][col] = "."

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(row, board:Board):
            if row == n:
                resp.append(board.get_state())
                return 
            
            for col in range(n):
                if board.in_col(row, col):
                    continue
                board.add_col(row, col)
                backtrack(row+1, board)
                board.remove_col(row, col)
        
        resp = []
        backtrack(0, Board(n))
        return resp