class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasMap = set()
        for n in nums:
            if n in hasMap:
                return True
            hasMap.add(n)
        return False