class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resp = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                return resp
            if i>0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1 
            while l< r:
                # if nums[l] ==a:
                #     l += 1
                #     continue
                z = a+nums[l] + nums[r]
                if z >0:
                    r -= 1
                elif z<0:
                    l += 1
                else:
                    resp.append([a, nums[l], nums[r]])
                    l += 1
                    r -=1 
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return resp