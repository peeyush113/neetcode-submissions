class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            
            m = (l+r)//2
            print(l, r, m)
            t = nums[m]
            if target < t:
                r = m-1
            elif target > t:
                l = m +1 
            else:
                return m
        return -1