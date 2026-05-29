class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = n-1
        k = m-1
        for i in range(m+n-1, -1, -1):
            if k<0 or j <0:
                break
            
            if nums1[k] > nums2[j]:
                nums1[i] = nums1[k]
                k -= 1
            else:
                nums1[i] = nums2[j]
                j -= 1
            
        for i in range(j, -1, -1):
            nums1[i] = nums2[i]
