class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        resp = nums[l]

        while l<=r:
            if nums[l] < nums[r]:
                resp = min(resp,  nums[l])
                break
            
            m = (l+r)//2
            resp = min(resp, nums[m])
            
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return resp

        
