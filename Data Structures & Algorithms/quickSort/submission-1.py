# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def sort(s, e):
            if e-s+1 <=1:
                return 

            p = pairs[e]
            l = s
            for i in range(s, e):
                if pairs[i].key < p.key:
                    tmp = pairs[l]
                    pairs[l] = pairs[i]
                    pairs[i] = tmp
                    l += 1
            pairs[e] = pairs[l]
            pairs[l] = p

            sort(s, l-1)
            sort(l+1, e)
        sort(0, len(pairs)-1)
        return pairs
