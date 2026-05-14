class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
         
        while r-l > 1:
            if nums[l] < nums[r]:
                return nums[l]
            

            m = ((l+r)//2)
            print(nums[l], nums[m], nums[r], end="-->")
            if nums[m] > nums[l]:
                if nums[r] > nums[m]:
                    return nums[l]
                else:
                    l = m+1
            else: 
                r = m
            print(nums[l], nums[r])
        return min(nums[r], nums[l])
