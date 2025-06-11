class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean_res = []
        maxCandy = max(candies)
        
        for i in range(len(candies)):
            boolean_res.append((candies[i] + extraCandies) >= maxCandy)
        return boolean_res