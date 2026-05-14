# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quick_sort_helper(self, piars, s, e):

        if (e-s+1) <= 1:
            return pairs
        
        p = piars[e]
        l = s

        for i in range(s, e):
            if pairs[i].key < p.key:
                tmp = pairs[l]
                pairs[l] = pairs[i]
                pairs[i] = tmp
                l += 1
        
        pairs[e] = pairs[l]
        pairs[l] = p
        
        self.quick_sort_helper(pairs, s, l-1)
        self.quick_sort_helper(pairs, l+1, e)
        
        return pairs


    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        self.quick_sort_helper(pairs, 0, len(pairs)-1) 
        
        return pairs