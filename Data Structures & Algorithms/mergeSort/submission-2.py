# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:


        def sort(s, e):
            if e-s+1 <=1:
                return

            m = (s+e)//2

            sort(s, m)
            sort(m+1, e)
            merge(s, m, e)
        
        def merge(s, m, e):
            L = pairs[s:m+1]
            R = pairs[m+1: e+1]

            l, r, p = 0, 0, s
            while l<len(L) and r<len(R):
                if L[l].key <= R[r].key:
                    pairs[p] = L[l]
                    l += 1
                else:
                    pairs[p] = R[r]
                    r += 1
                p += 1
            
            while l<len(L):
                pairs[p] = L[l]
                p += 1
                l +=1 
            while r<len(R):
                pairs[p] = R[r]
                p += 1
                r += 1
        sort(0, len(pairs))
        return pairs