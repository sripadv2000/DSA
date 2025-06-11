class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = candies[0]
        length = len(candies)
        for i in range(1, length):
            max_candy = max(max_candy, candies[i])
        boolean_res = []
        for i in range(length):
            if (candies[i] + extraCandies) >= max_candy:
                boolean_res.append(True)
            else:
                boolean_res.append(False)
        return boolean_res