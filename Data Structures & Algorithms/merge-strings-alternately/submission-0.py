class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x, y, s = 0, 0, ""

        while x<len(word1) or y<len(word2):
            if x<len(word1):
                s = s + word1[x]
                x += 1
            
            if y < len(word2):
                s += word2[y]
                y += 1
        return s