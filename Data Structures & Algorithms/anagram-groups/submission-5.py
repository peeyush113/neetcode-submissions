
def quickSort(strs):
    strs = list(strs)
    def helper(s, e):
        if e-s+1<=0+1:
            return 
        
        p = ord(strs[e])
        l = s
    
        for i in range(s, e):
            if ord(strs[i]) < p:
                tmp = strs[l]
                strs[l] = strs[i]
                strs[i] = tmp
                l += 1

        tmp = strs[e]
        strs[e] = strs[l]
        strs[l] = tmp
        
        helper(l+1, e)
        helper(s, l-1)
    helper(0, len(strs)-1)
    return "".join(strs) 



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            st = quickSort(s)
            print(st, s)
            hm.setdefault(st, []).append(s)
        
        print(hm)
        return list(hm.values())



