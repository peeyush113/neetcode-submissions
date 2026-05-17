class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for a in strs:
            b = "".join(sorted(a)) 
            hash_map.setdefault(b, []).append(a)
        return list(hash_map.values())