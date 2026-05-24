class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        l = min([len(n) for n in strs])
        for i in range(l):
            v = strs[0][i]
            for s in strs[1:]:
                if s[i] != v:
                    return prefix
            prefix += v
        return prefix