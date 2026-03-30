class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[j]<=prices[i]:
                    result[i]=prices[i]-prices[j]
                    break
        return result
