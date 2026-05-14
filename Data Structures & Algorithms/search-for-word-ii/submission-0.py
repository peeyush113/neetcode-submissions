
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    def addWord(self, word):
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.addWord(word)

        row, col = len(board), len(board[0])
        resp, visited = set(), set()

        def dfs(i, j,  node, char):
            if (i<0 or j<0 or i==row or j==col 
                or (i, j) in visited 
                or board[i][j] not in node.children):
                return 
            visited.add((i, j))
            w = board[i][j]
            node = node.children[w]
            char += w
            if node.word:
                resp.add(char)
            
            dfs(i, j+1, node, char)
            dfs(i+1, j, node, char)
            dfs(i-1, j, node, char)
            dfs(i, j-1, node, char)
            
            visited.remove((i, j)) 


        for i in range(row):
            for j in range(col):
                dfs(i,j, t.head, "")

        return list(resp)


