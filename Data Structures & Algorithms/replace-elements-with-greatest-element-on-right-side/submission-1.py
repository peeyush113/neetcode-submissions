class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            t = arr[i]
            arr[i] = tmp
            if t > tmp:
                tmp = t
            
        return arr
