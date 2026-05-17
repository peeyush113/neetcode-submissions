class NumArray:

    def __init__(self, nums: List[int]):
        self.sumArray = []
        prev_sum = 0
        for n in nums:
            prev_sum += n
            self.sumArray.append(prev_sum)
        print(self.sumArray)    

    def sumRange(self, left: int, right: int) -> int:
        left -= 1
        if left >= 0:
            return self.sumArray[right] - self.sumArray[left]
        else:
            return self.sumArray[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)