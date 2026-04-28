class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPurchase = prices[0]

        for price in prices:
            profit = max(profit, price - minPurchase)
            minPurchase = min(price, minPurchase)
        return profit
