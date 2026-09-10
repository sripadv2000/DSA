class Solution:
    def countCommas(self, n):
        if n < 1000:
            return 0
        
        totalCommas = 0
        start = 1000

        while start <= n:
            totalCommas += n - start + 1
            start *= 1000
        
        return totalCommas