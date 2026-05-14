class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[target-nums[i]] = i
        print(hm.keys())
        for i in range(len(nums)):
            j = hm.get(nums[i], -1)
            if j>=0 and i!=j:
                return [i, j]
        return 