class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)

        l, r = 0, len(nums)-1
        psum = 1
        ssum = 1

        while l < len(nums):
            prefix[l] = psum
            suffix[r] = ssum


            psum *= nums[l]
            ssum *= nums[r]
            l += 1
            r -= 1
        resp = []
        for i in range(len(nums)):
            resp.append(prefix[i]*suffix[i])
        return resp
