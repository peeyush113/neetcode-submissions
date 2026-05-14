class Solution:
    def reverseBits(self, n: int) -> int:
        place_value = 31
        res = 0
        while n>0:
            a = n & 1
            res += a * pow(2, place_value)
            place_value -= 1
            n = n>>1
        return res