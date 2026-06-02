class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, p = 0, 1, 0

        while r < len(prices):
            p = max(prices[r]-prices[l], p)
            if prices[r] < prices[l]:
                l = r
            r += 1
                
        return p
