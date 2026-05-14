class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = []
        for n in nums:
            if n in hm:
                return True
            hm.append(n)
        return False
