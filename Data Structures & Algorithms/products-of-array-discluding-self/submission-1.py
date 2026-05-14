class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preP = [1]
        t = 1
        for i in range(len(nums)-1):
            t = t*nums[i]
            preP.append(t)
        
        
        postP = [1]*len(nums)
        t = 1
        for i in range(len(nums)-1, 0, -1):
            t = t*nums[i]
            postP[i-1] = t
        print(preP, postP)
        resp = []
        for i in range(len(nums)):
            resp.append(preP[i]*postP[i])
        
        return resp
        
        

