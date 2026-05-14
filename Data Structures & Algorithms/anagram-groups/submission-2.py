class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for b in strs:
            p = "".join(sorted(b)) 
            a.setdefault(p, []).append(b)
        
        return list(a.values())