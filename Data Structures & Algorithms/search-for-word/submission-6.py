class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(r, c, w):
            if board[r][c] != word[w]:
                return False

            if w == len(word)-1:
                return True
                        
            visited.add((r, c))

            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if min(nr, nc) < 0 or nr > len(board)-1 or nc > len(board[0])-1 or (nr, nc) in visited:
                    continue
                
                if backtrack(nr, nc, w+1):
                    return True
            visited.remove((r, c))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                # visited.add((row, col))
                # if board[row][col] == word[0] and backtrack(row, col, 0):
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True
                # visited.remove((row, col))
        return False