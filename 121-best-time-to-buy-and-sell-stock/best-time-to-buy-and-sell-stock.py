class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        N = len(prices)
        for i in range(1, N):
                buy = min(buy, prices[i])
                max_profit = max(max_profit, prices[i] - buy)
        return max_profit