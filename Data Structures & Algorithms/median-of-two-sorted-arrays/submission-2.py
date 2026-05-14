class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            median_index = length//2
        else:
            median_index = (length//2)
        
        sorted_list = []
        i, j = 0, 0 
        while median_index > len(sorted_list)-1 and i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_list.append(nums1[i])
                i += 1
            else:
                sorted_list.append(nums2[j])
                j += 1
        
        while median_index > len(sorted_list)-1 and i < len(nums1):
            sorted_list.append(nums1[i])
            i += 1
        while median_index > len(sorted_list)-1 and j < len(nums2):
            sorted_list.append(nums2[j])
            j += 1

        print(sorted_list, median_index, length)
        if length % 2 == 0:
            return (sorted_list.pop()+sorted_list.pop())/2
        else:
            return sorted_list.pop()
