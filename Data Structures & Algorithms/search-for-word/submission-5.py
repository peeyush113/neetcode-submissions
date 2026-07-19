class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(r, c, w):
            if w == len(word)-1:
                # print(board[r][c], word[w], r, c, w)
                return True
            w += 1
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if min(nr, nc) < 0 or nr > len(board)-1 or nc > len(board[0])-1 or (nr, nc) in visited:
                    continue
                
                if board[nr][nc] == word[w]:
                    visited.add((nr, nc))
                    if backtrack(nr, nc, w):
                        print(board[nr][nc], word[w], nr, nc, w)
                        return True
                    visited.remove((nr, nc))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                visited.add((row, col))
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    print(board[row][col], word[0], row, col)
                    return True
                visited.remove((row, col))
        return False