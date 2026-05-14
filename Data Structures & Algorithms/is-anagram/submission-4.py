class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.setdefault(s[i], 0) + 1
            seen[t[i]] = seen.setdefault(t[i], 0) - 1
        return set(seen.values()) == {0}
