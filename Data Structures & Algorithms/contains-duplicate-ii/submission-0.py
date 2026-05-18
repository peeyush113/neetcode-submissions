class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in a:
                return True
            else:
                a.add(nums[r])
            if len(a) >k:
                a.remove(nums[l])
                l += 1
        return False