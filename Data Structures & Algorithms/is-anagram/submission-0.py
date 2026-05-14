class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map = {}
        for n in s:
            hash_map.setdefault(n, 0)
            hash_map[n] += 1
        
        for n in t:
            if n not in hash_map:
                return False
            
            hash_map[n] -= 1
        
        for k, v in hash_map.items():
            if v > 0:
                return False
        
        return True