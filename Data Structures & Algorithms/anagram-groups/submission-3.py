class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for s in strs:
            count = [0]*26
            for c in s:
                k = ord(c) - ord("a")
                count[k] += 1 
            a.setdefault(tuple(count), []).append(s)
        
        return list(a.values())