class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        resp = 0
        for n in nums:
            resp = n ^ resp
        return resp