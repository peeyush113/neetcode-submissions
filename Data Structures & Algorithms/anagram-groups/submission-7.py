class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for a in strs:
            count = [0] *26
            for i in a:
                p = ord(i) - ord("a")
                count[p] += 1
            hash_map.setdefault(tuple(count), []).append(a)
        return list(hash_map.values())