class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            
            m = (l+r)//2
            left, right, mid = nums[l], nums[r], nums[m]
            print(left, right, mid)
            if target == mid:
                return m

            if left <= mid:
                # left sorted portion
                if target > mid or target < left:
                    l = m +1 
                else:
                    r = m -1
            else:
                # right sorted portion
                if target < mid or target > right:
                    r = m -1
                else:
                    l = m + 1
            print(l, r, m)
        return -1 

