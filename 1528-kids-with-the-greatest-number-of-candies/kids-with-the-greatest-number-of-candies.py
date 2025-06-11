class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = candies[0]
        length = len(candies)
        boolean_res = []

        for i in range(1, length):
            maxCandy = max(maxCandy, candies[i])
        
        for i in range(length):
            if (candies[i] + extraCandies) >= maxCandy:
                boolean_res.append(True)
            else:
                boolean_res.append(False)
        return boolean_res