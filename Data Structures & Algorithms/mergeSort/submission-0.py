# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def merge(self, arr, s, m, e):
        l = arr[s:m+1]
        r = arr[m+1:e+1]

        i, j, k = 0, 0, s

        while i <len(l) and j < len(r):
            if l[i].key <= r[j].key:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1

            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

        return arr

    def merge_sort_help(self, arr, s, e):
        if (e-s+1<=1):
            return arr
        
        m = (s+e)//2

        self.merge_sort_help(arr, s, m)
        self.merge_sort_help(arr, m+1, e)

        self.merge(arr, s, m, e)
        return arr


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        return self.merge_sort_help(pairs, 0, len(pairs))
