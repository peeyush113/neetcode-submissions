class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            if n in hash:
                return [min(hash[n]), i]
            v = target - n
            hash.setdefault(v, []).append(i)
        
