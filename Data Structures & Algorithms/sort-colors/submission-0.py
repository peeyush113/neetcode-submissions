class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        hash = [0, 0, 0]
        for n in nums:
            hash[n] +=1 
        
        i = 0
        for k, n in enumerate(hash):
            for j in range(i, i+n):
                nums[j] = k
            i += n
        