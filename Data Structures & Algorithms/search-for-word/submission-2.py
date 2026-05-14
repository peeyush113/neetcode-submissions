class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        resp = False
        R, C = len(board)-1, len(board[0])-1
        wl = len(word)
        def backtracking(i, j, cur, visited):
            
            if cur != word[:len(cur)]:
                return False
            print(i, j, cur)
            if len(cur) == wl:
                if cur == word:
                    return True
                else:
                    return False
            
            for k,l in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                m, n = i+k, j+l
                if m < 0 or n<0 or m>R or n>C or (m,n) in visited:
                    continue
                visited.append((i, j))
                if backtracking(m, n, cur+board[m][n], visited):
                    return True
                visited.pop()
            return False

        for r in range(R+1):
            for c in range(C+1):
                if backtracking(r, c, board[r][c], []):
                    return True
             
        return False
