class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        lenght = 1
        curr_len = 1
        for i in range(len(nums)):
            if prev == nums[0]:
                prev = heapq.heappop(nums)
                continue
            if prev+1 == nums[0]:
                curr_len += 1
                lenght = max(curr_len, lenght)
            else:
                curr_len = 1
            # print(prev, lenght, curr_len, nums)
            prev = heapq.heappop(nums)
        return lenght