class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <=r:
            m = (l+r)//2
            nl, nr, nm = nums[l], nums[r], nums[m]
            if nm <nr:
                r = m
            elif nm >nr:
                l = m+1
            else:
                return nm