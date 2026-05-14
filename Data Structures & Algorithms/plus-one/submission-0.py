class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        cary = 1
        for i in range(len(digits)-1, -1, -1):
            d = digits[i]+cary
            digits[i] = d%10
            cary = d//10
        if cary:
            digits = [cary]+digits
        return digits