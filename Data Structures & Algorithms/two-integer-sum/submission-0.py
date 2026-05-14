class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i, n in enumerate(nums) :
            if n in hash_map:
                return [hash_map[n], i]
            
            hash_map[target-n] = i
            
