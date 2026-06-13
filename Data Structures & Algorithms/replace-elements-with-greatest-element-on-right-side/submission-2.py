class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = -1

        for i in range(len(arr)-1, -1, -1):
            t = arr[i]
            arr[i] = tmp
            tmp = max(tmp, t)
            
        return arr
