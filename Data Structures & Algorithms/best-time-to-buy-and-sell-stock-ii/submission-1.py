class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0)
        profit = 0
        buy_price = -1
        for i in range(len(prices)-1):
            price = prices[i]
            if price > prices[i+1]:
                if buy_price >-1 :
                    profit = profit+ (price-buy_price)
                    buy_price = -1
            else:
                if buy_price == -1:
                    buy_price = price
            print(i, buy_price, profit, price, prices[i+1])
        return profit