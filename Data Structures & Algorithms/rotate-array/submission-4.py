class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        tmp = []
        r = len(nums)-1
        for i in range(k, 0, -1):
            tmp.append(nums[r])
            r -= 1

        end = len(nums)-1
        while r >-1:
            nums[end] = nums[r]
            r -= 1
            end -= 1
        l = 0
        while end >-1:
            nums[end] = tmp[l]
            end -= 1
            l +=1