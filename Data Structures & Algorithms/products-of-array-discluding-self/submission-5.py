class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a, b = [1]*len(nums), [1]*len(nums)
        
        r = len(nums)-2
        for l in range(1, len(nums)):
            a[l] = a[l-1]*nums[l-1]
            b[r] = b[r+1]*nums[r+1]
            r -=1 

        for i in range(len(nums)):
            nums[i] = a[i]*b[i]

        return nums