class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        p = l
        
        if nums[0] <= target <= nums[p-1] and p>0:
            l, r = 0, p-1
        else:
            l, r = p, len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if nums[m]<target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
        return -1
        

