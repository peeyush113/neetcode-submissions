class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for w in s:
            hash.setdefault(w, 0)
            hash[w] += 1
        
        for w in t:
            if w not in hash:
                return False
            hash[w] -=1 
            if hash[w] ==0:
                del hash[w]
        return hash == {}
            
