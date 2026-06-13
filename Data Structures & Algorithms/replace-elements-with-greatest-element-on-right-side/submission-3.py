class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], tmp = tmp, max(tmp, arr[i])
            
        return arr
