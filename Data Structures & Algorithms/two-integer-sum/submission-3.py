class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i, n in enumerate(nums):
            if n in track:
                return [track[n], i]
            else:
                track[target-n] = i
