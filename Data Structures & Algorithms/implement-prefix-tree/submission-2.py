class Trie:
     def __init__(self, word=False) -> None:
         self.map = {}
         self.word = word

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        
        curr = self.root
        for w in word:
            if w not in curr.map:
                curr.map[w] = Trie()
            curr = curr.map[w]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            if w not in curr.map:
                return False
            curr = curr.map[w]
        return curr.word


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for w in prefix:
            if w not in curr.map:
                return False
            curr = curr.map[w]
        return True
        