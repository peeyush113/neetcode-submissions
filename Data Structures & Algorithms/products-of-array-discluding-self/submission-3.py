class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        resp = [1]*len(nums)
        for i in range(len(nums)):
            resp[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            resp[i] *= suffix
            suffix *= nums[i]
        return resp
