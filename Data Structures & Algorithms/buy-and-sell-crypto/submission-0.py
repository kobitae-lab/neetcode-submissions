class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        for i in range(len(prices)):
            current_max = max((max(prices[i:]) - prices[i]), current_max)
        return current_max
