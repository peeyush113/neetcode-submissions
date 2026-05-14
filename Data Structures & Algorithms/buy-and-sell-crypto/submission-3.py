class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        for r in range(1, len(prices)):
            right = prices[r]
            left = prices[l]
            p = right - left
            print(l, left, r, right, p)
            profit = max(profit, p)
            if p<0:
                l = r
        return profit