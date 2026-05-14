class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in nums:
            if hash_map.get(i, 0) > 0:
                return True
            else:
                hash_map[i] = 1
        return False