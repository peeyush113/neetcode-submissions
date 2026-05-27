class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a, b = [1]*len(nums), [1]*len(nums)
        k, v = 1, 1
        r = len(nums)-1
        for l in range(len(nums)):
            a[l] = k
            k = k*nums[l]
            b[r] = v
            v = v * nums[r]
            r -=1 
        for i in range(len(nums)):
            nums[i] = a[i]*b[i]

        return nums