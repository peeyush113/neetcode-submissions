class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {}
        for i in range(len(s)):
            w, v = s[i], t[i]
            
            hash.setdefault(w, 0)
            hash[w] += 1

            hash.setdefault(v, 0)
            hash[v] -= 1 

        for v in hash.values():
            if v != 0:
                return False

        return True
            
