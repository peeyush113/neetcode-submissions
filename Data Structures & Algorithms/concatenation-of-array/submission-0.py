class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        resp = []
        for j in range(2):
            for n in nums:
                resp.append(n)
        return resp